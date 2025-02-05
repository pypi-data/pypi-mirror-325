import hashlib
import logging
from collections.abc import Iterator

import attrs
import lance
import pyarrow as pa

from geneva.checkpoint import (
    CheckpointStore,
)
from geneva.debug.logger import ErrorLogger, NoOpErrorLogger
from geneva.query import Scan
from geneva.transformer import UDF

_LOG = logging.getLogger(__name__)


@attrs.define
class ReadTask:
    uri: str
    columns: list[str]
    frag_id: int
    offset: int
    limit: int

    filter: str | None = None

    batch_size: int = 1024

    def to_batches(self) -> Iterator[pa.RecordBatch]:
        uri_parts = self.uri.split("/")
        name = ".".join(uri_parts[-1].split(".")[:-1])
        db = "/".join(uri_parts[:-1])
        scan = (
            Scan.from_uri(db, name)
            .with_columns(self.columns)
            .with_fragments([self.frag_id])
            .with_filter(self.filter)
            .with_offset(self.offset)
            .with_limit(self.limit)
        )
        yield from scan.to_batches(self.batch_size)

    def checkpoint_key(self) -> str:
        hasher = hashlib.md5()
        hasher.update(
            f"{self.uri}:{self.frag_id}:{self.offset}:{self.limit}:{self.filter}".encode(),
        )
        return hasher.hexdigest()


@attrs.define
class LanceRecordBatchUDFApplier:
    udfs: dict[str, UDF] = attrs.field()
    checkpoint_store: CheckpointStore = attrs.field()
    error_logger: ErrorLogger = attrs.field(default=NoOpErrorLogger())

    @property
    def output_schema(self) -> pa.Schema:
        return pa.schema(
            [pa.field(name, fn.data_type) for name, fn in self.udfs.items()],
        )

    def _run(self, task: ReadTask) -> pa.RecordBatch:
        data_key = task.checkpoint_key()
        _LOG.debug("Running task %s", task)
        # track the batch sequence number so we can checkpoint any errors
        # when reproducing locally we can seek to the erroring batch quickly

        # prepare the schema
        fields = []
        for name, fn in self.udfs.items():
            fields.append(pa.field(name, fn.data_type, metadata=fn.field_metadata))
        schema = pa.schema(fields)

        res = {}
        batch = None
        for name, fn in self.udfs.items():
            checkpoint_key = f"{data_key}:{fn.checkpoint_key}"
            if checkpoint_key in self.checkpoint_store:
                _LOG.info("Using cached result for %s", checkpoint_key)
                res[name] = self.checkpoint_store[checkpoint_key][
                    "data"
                ].combine_chunks()  # type: ignore
                continue
            arrs = []
            # TODO: add caching for the input data
            for seq, batch in enumerate(task.to_batches()):
                try:
                    arrs.append(fn(batch))
                except Exception as e:
                    self.error_logger.log_error(e, task, fn, seq)
                    raise e

            arr = pa.concat_arrays(arrs)
            self.checkpoint_store[checkpoint_key] = pa.RecordBatch.from_pydict(
                {"data": arr},
            )
            res[name] = arr

        return pa.RecordBatch.from_pydict(res, schema=schema)

    def run(self, task: ReadTask) -> pa.RecordBatch:
        try:
            return self._run(task)
        except Exception as e:
            logging.exception("Error running task %s: %s", task, e)
            raise RuntimeError(f"Error running task {task}") from e

    def status(self, task: ReadTask) -> dict[str, str]:
        data_key = task.checkpoint_key()
        return {
            name: f"{data_key}:{fn.checkpoint_key}" in self.checkpoint_store
            for name, fn in self.udfs.items()
        }  # type: ignore


def plan_read(
    uri: str,
    columns: list[str] | None = None,
    *,
    read_version: int | None = None,
    batch_size: int = 1024,
    filter: str | None = None,  # noqa: A002
    num_tasks: int = 2048,
) -> Iterator[ReadTask]:
    """Make Plan for Reading Data from a Dataset"""
    if columns is None:
        columns = []
    dataset = lance.dataset(uri)
    if read_version is not None:
        dataset = dataset.checkout(read_version)

    total_rows = dataset.count_rows(filter=filter)
    rows_per_task = max(total_rows // num_tasks + 1, batch_size)

    for frag in dataset.get_fragments():
        frag_rows = frag.count_rows(filter=filter)
        for offset in range(0, frag_rows, rows_per_task):
            limit = min(rows_per_task, frag_rows - offset)
            yield ReadTask(
                uri=uri,
                columns=columns,
                frag_id=frag.fragment_id,
                batch_size=batch_size,
                offset=offset,
                limit=limit,
                filter=filter,
            )

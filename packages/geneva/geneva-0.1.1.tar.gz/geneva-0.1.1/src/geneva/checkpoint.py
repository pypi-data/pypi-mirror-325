# checkpointing utils for lancedb

import abc
import logging
import os
from collections.abc import Iterator

import pyarrow as pa
from pyarrow import fs

_LOG = logging.getLogger(__name__)


class CheckpointStore(abc.ABC):
    """Abstract class for checkpoint store, which is a key-value store for storing
    pyarrow.RecordBatch objects

    This is a lighter weight version of collections.abc.MutableMapping
    where we don't expose length or deletion operations
    """

    @abc.abstractmethod
    def __contains__(self, item: str) -> bool:
        pass

    @abc.abstractmethod
    def __getitem__(self, item: str) -> pa.RecordBatch:
        pass

    @abc.abstractmethod
    def __setitem__(self, key: str, value: pa.RecordBatch) -> None:
        pass

    @abc.abstractmethod
    def list_keys(self, prefix: str = "") -> Iterator[str]:
        pass

    @classmethod
    def from_uri(cls, uri: str) -> "CheckpointStore":
        """Construct a CheckpointStore from a URI."""
        if uri == "memory":
            return InMemoryCheckpointStore()
        if uri.startswith(("s3://", "gs://", "az://", "file://")):
            return ArrowFsCheckpointStore(uri)
        raise ValueError(f"Invalid checkpoint store uri: {uri}")


class InMemoryCheckpointStore(CheckpointStore):
    """In memory checkpoint store for testing purposes."""

    def __init__(self) -> None:
        self._store = {}

    def __contains__(self, item: str) -> bool:
        return item in self._store

    def __getitem__(self, item: str) -> pa.RecordBatch:
        return self._store[item]

    def __setitem__(self, key: str, value: pa.RecordBatch) -> None:
        self._store[key] = value

    def list_keys(self, prefix: str = "") -> Iterator[str]:
        for key in self._store:
            if key.startswith(prefix):
                yield key


class ArrowFsCheckpointStore(CheckpointStore):
    def __init__(self, root: str) -> None:
        self.fs, self.path = fs.FileSystem.from_uri(root)  # type: ignore

    def __contains__(self, item: str) -> bool:
        _LOG.debug("contains: %s", item)
        info = self.fs.get_file_info(os.path.join(self.path, item))
        return info.type != fs.FileType.NotFound

    def __getitem__(self, item: str) -> pa.RecordBatch:
        _LOG.debug("get: %s", item)
        with (
            self.fs.open_input_file(os.path.join(self.path, item)) as f,
            pa.RecordBatchFileReader(f) as r,
        ):
            return r.read_all().combine_chunks()

    def __setitem__(self, key: str, value: pa.RecordBatch) -> None:
        _LOG.debug("set: %s", key)
        with (
            self.fs.open_output_stream(os.path.join(self.path, key)) as f,
            pa.RecordBatchFileWriter(
                f,
                value.schema,
            ) as writer,
        ):
            writer.write(value)

    def list_keys(self, prefix: str = "") -> Iterator[str]:
        _LOG.debug("list_keys: %s", prefix)
        selector = fs.FileSelector(os.path.join(self.path, prefix))
        for file in self.fs.get_file_info(selector):
            yield file.path.removeprefix(self.path).lstrip("/")

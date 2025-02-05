# Use lance lake with Google Dataflow

import logging
import os
import uuid

try:
    import apache_beam as beam
    from apache_beam.options.pipeline_options import (
        PipelineOptions,
        SetupOptions,
        StandardOptions,
    )
except ImportError as err:
    raise ImportError(
        "apache_beam is required for this module, pip install geneva[dataflow]",
    ) from err

import lance
import pyarrow as pa

from geneva.apply import LanceRecordBatchUDFApplier, plan_read
from geneva.checkpoint import CheckpointStore
from geneva.debug.logger import CheckpointStoreErrorLogger
from geneva.runners.dataflow.reshuffle import ReshuffleByFragmentChunks
from geneva.transformer import UDF

_LOG = logging.getLogger(__name__)


def get_dataflow_options(opts: dict[str, str] | None) -> dict[str, str]:
    """Load Dataflow Options"""
    dataflow_options = {}
    dataflow_options["runner"] = opts.get(
        "runner",
        os.environ.get("LANCE_DATAFLOW_RUNNER"),
    )
    dataflow_options["region"] = opts.get(
        "region",
        os.environ.get("LANCE_DATAFLOW_REGION"),
    )
    dataflow_options["project"] = opts.get(
        "project",
        os.environ.get("LANCE_DATAFLOW_PROJECT"),
    )
    dataflow_options["temp_location"] = opts.get(
        "temp_location",
        os.environ.get("LANCE_DATAFLOW_TEMP_LOCATION"),
    )
    dataflow_options["staging_location"] = opts.get(
        "staging_location",
        os.environ.get("LANCE_DATAFLOW_STAGING_LOCATION"),
    )
    dataflow_options["docker_image"] = opts.get(
        "docker_image",
        os.environ.get("LANCE_DATAFLOW_DOCKER_IMAGE"),
    )
    dataflow_options["disk_size_gb"] = opts.get(
        "disk_size_gb",
        os.environ.get("LANCE_DATAFLOW_DISK_SIZE_GB", "100"),
    )
    dataflow_options["machine_type"] = "n2-highmem-16"
    return dataflow_options


def map_with_value(  # noqa: ANN201
    fn: UDF,
):
    def _wrapped(x):  # noqa: ANN202
        return x, fn(x)

    return _wrapped


def extract_frag_id_as_key(x):  # noqa: ANN201
    return x[0].frag_id, x


def write_fragment(  # noqa: ANN201
    uri: str,
):
    dataset = lance.dataset(uri)

    def _write_fragment(x):  # noqa: ANN202
        frag_id, batch = x
        batch: pa.RecordBatch = batch
        # make sure metadata isn't dropped
        assert len(batch.schema.names) == 1
        new_arr = batch.columns[0]
        new_col_name = batch.schema.names[0]

        old_data: pa.Table = dataset.get_fragment(frag_id).to_table()

        t = pa.Table.from_pydict(
            {
                col: old_data[col] if col != new_col_name else new_arr
                for col in old_data.schema.names
            }
        )

        dataset.merge_insert(
            x for x in old_data.column_names if x != new_col_name
        ).when_matched_update_all().execute(t)

    return _write_fragment


def sort_and_collect_batch(x):  # noqa: ANN201
    (frag_id, data) = x
    data.sort(key=lambda x: x[0].offset)

    batches = [x[1] for x in data]
    batches = (
        pa.Table.from_batches(batches, schema=batches[0].schema)
        .combine_chunks()
        .to_batches()
    )
    assert len(batches) == 1, "pa table should have been coalesced to a single batch"
    return frag_id, batches[0]


def run_dataflow_add_column(
    uri: str,
    columns: list[str],
    transforms: dict[str, UDF],
    checkpoint_store: CheckpointStore,
    /,
    job_id: str | None = None,
    batch_size: int = 8,
    read_version: int | None = None,
    dataflow_options: dict[str, str] | None = None,
    test_run: bool = True,
    **kwargs,
) -> beam.Pipeline | None:
    pipeline_args = [
        "--runner",
        dataflow_options["runner"],
        "--project",
        dataflow_options["project"],
        "--region",
        dataflow_options["region"],
        "--temp_location",
        dataflow_options["temp_location"],
        "--staging_location",
        dataflow_options["staging_location"],
        "--experiments=use_runner_v2",
        "--disk_size_gb=" + dataflow_options["disk_size_gb"],
    ]
    if dataflow_options["docker_image"]:
        pipeline_args += [
            "--sdk_container_image=" + dataflow_options["docker_image"],
        ]

    try:
        import prefect
        from prefect.exceptions import MissingContextError

        try:
            job_id = job_id or prefect.context.get_run_context().flow_run.id
            _LOG.info("Using prefect job id: %s", job_id)
        except MissingContextError:
            job_id = None
    except ImportError:
        job_id = None

    job_id = job_id or uuid.uuid4().hex

    # We use the save_main_session option because one or more DoFn's in this
    # workflow rely on global context (e.g., a module imported at module level).
    pipeline_options = PipelineOptions(pipeline_args)
    # we usually submit from a local environment, don't want save the main session
    pipeline_options.view_as(SetupOptions).save_main_session = False
    # otherwise __exit__ will wait for the job to finish
    pipeline_options.view_as(StandardOptions).no_wait_until_finish = True

    applier = LanceRecordBatchUDFApplier(
        udfs=transforms,
        checkpoint_store=checkpoint_store,
        error_logger=CheckpointStoreErrorLogger(job_id, checkpoint_store),
    )

    if read_version is None:
        read_version = lance.dataset(uri).version

    if test_run:
        tasks = [next(plan_read(uri, columns, batch_size=batch_size))]
    else:
        tasks = list(plan_read(uri, columns, batch_size=batch_size))

    if not len(tasks):
        return None

    # The pipeline will be run on exiting the with block.
    with beam.Pipeline(options=pipeline_options) as p:
        _ = (
            p
            | beam.Create(tasks)
            | ReshuffleByFragmentChunks()
            | "Apply UDFs" >> beam.Map(map_with_value(applier.run))
            | "ExtractFragID" >> beam.Map(extract_frag_id_as_key)
            | "GroupByKey" >> beam.GroupByKey()
            | "SortAndCollectBatch" >> beam.Map(sort_and_collect_batch)
            | "WriteFragments" >> beam.Map(write_fragment(uri))
        )

    return p

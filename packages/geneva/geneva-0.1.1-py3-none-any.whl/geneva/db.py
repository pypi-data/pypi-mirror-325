import os
from collections.abc import Iterable
from functools import cached_property
from pathlib import Path
from typing import TYPE_CHECKING

import lancedb
import pyarrow as pa
from lancedb import DBConnection
from lancedb.common import DATA, Credential
from lancedb.pydantic import LanceModel
from overrides import override

from geneva.checkpoint import CheckpointStore
from geneva.remote.client import RestfulLanceDBClient

if TYPE_CHECKING:
    from geneva.job.client import JobClient
    from geneva.table import Table


class Connection(DBConnection):
    """Lance DataLake Connection."""

    def __init__(
        self,
        uri: str,
        *,
        region: str = "us-east-1",
        api_key: Credential | None = None,
        host_override: str | None = None,
        storage_options: dict[str, str] | None = None,
        checkpoint_store: CheckpointStore | None = None,
        dataflow_options: dict[str, str] | None = None,
        **kwargs,
    ) -> None:
        super().__init__()
        self._uri = uri
        self._region = region
        self._api_key = api_key
        self._host_override = host_override
        self._storage_options = storage_options
        self._ldb: DBConnection | None = None
        self._checkpoint_store = checkpoint_store

        # Dataflow Options
        self._dataflow_options = dataflow_options

    def __repr__(self) -> str:
        return f"<LanceLake uri={self.uri}>"

    def __getstate__(self) -> dict:
        return {
            "uri": self._uri,
            "api_key": self._api_key,
            "host_override": self._host_override,
            "storage_options": self._storage_options,
            "region": self._region,
        }

    def __setstate__(self, state) -> None:
        self.__init__(state.pop("uri"), **state)

    @cached_property
    def _connect(self) -> DBConnection:
        """Returns the underlying lancedb connection."""
        if self._ldb is None:
            self._ldb = lancedb.connect(
                self.uri,
                region=self._region,
                api_key=self._api_key,
                host_override=self._host_override,
                storage_options=self._storage_options,
            )
        return self._ldb

    @cached_property
    def _client(self) -> RestfulLanceDBClient:
        if (self._api_key is None) or (self._region is None):
            raise ValueError("API Key and Region must be provided.")

        return RestfulLanceDBClient(
            db_name=self._uri.removeprefix("db://"),
            region=self._region,
            api_key=self._api_key,
            host_override=self._host_override,
        )

    @override
    def table_names(
        self,
        page_token: str | None = None,
        limit: int | None = None,
    ) -> Iterable[str]:
        return self._connect.table_names(page_token=page_token, limit=limit or 10)

    @override
    def open_table(
        self,
        name: str,
        *,
        storage_options: dict[str, str] | None = None,
        index_cache_size: int | None = None,
    ) -> "Table":
        """Open a Lance Table.

        Parameters
        ----------
        name: str
            Name of the table.

        """
        from .table import Table

        storage_options = storage_options or self._storage_options

        return Table(
            self,
            name,
            index_cache_size=index_cache_size,
            storage_options=storage_options,
        )

    @override
    def create_table(  # type: ignore
        self,
        name: str,
        data: DATA | None = None,
        schema: pa.Schema | LanceModel | None = None,
        mode: str = "create",
        exist_ok: bool = False,
        on_bad_vectors: str = "error",
        fill_value: float = 0.0,
        *,
        storage_options: dict[str, str] | None = None,
        **kwargs,
    ) -> "Table":  # type: ignore
        from .table import Table

        self._connect.create_table(
            name,
            data,
            schema,
            mode,
            exist_ok=exist_ok,
            on_bad_vectors=on_bad_vectors,
            fill_value=fill_value,
            storage_options=storage_options,
            **kwargs,
        )
        return Table(self, name, storage_options=storage_options)

    def create_view(
        self,
        name: str,
        query: str,
        materialized: bool = False,
    ) -> "Table":
        """Create a View from a Query.

        Parameters
        ----------
        name: str
            Name of the view.
        query: Query
            Query to create the view.
        materialized: bool, optional
            If True, the view is materialized. Default is False.

        TODO: replace Query with a SQL string?
        TODO: this should be handled by the backend.

        """
        raise NotImplementedError("Create view is not implemented yet")

    def drop_view(self, name: str) -> None:
        """Drop a view."""
        raise NotImplementedError("Drop view is not implemented yet")

    @cached_property
    def jobs(self) -> "JobClient":
        """Jobs API.

        Example
        -------

        # List all jobs
        >>> conn = connect("db://mydb")
        >>> jobs = conn.jobs.list(table="mytable",
            limit=500,
            filter="created_at > '2021-01-01'")

        # Start a new job
        >>> conn.jobs.start(table="mytable", column="virtual_col")
        """
        from geneva.job.client import JobClient

        return JobClient(rest_client=self._client)


def connect(
    uri: str | Path,
    *,
    region: str = "us-east-1",
    api_key: Credential | None = None,
    override_host: str | None = None,
    storage_options: dict[str, str] | None = None,
    checkpoint: str | CheckpointStore | None = None,
    dataflow_options: dict[str, str] | None = None,
    **kwargs,
) -> Connection:
    """Connect to Lance DataLake.

    Parameters
    ----------
    uri: datalake URI, or Path

    checkpoint: str or CheckpointStore, optional
        Checkpoint store for the connection. If not provided, will try to read from
        envvar "LANCE_CHECKPOINT", or from a configuration file.
    dataflow_options : dict, optional
        If use dataflow engine, specify the options here.

    """
    if checkpoint is None:
        checkpoint = os.getenv("LANCE_CHECKPOINT", "memory")
    if isinstance(checkpoint, str):
        checkpoint_store = CheckpointStore.from_uri(checkpoint)
    else:
        checkpoint_store = checkpoint
    return Connection(
        str(uri),
        region=region,
        api_key=api_key,
        override_host=override_host,
        storage_options=storage_options,
        checkpoint_store=checkpoint_store,
        dataflow_options=dataflow_options,
        **kwargs,
    )

from typing import List

from pydantic import BaseModel

from polly.sources.enum import DataSourceType


class ConnectionConfig(BaseModel):
    host: str
    port: int
    user: str
    password: str
    database: str = ""
    collections: List[str] = []


class SourceConfig(BaseModel):
    name: str
    type: DataSourceType
    connection_config: ConnectionConfig

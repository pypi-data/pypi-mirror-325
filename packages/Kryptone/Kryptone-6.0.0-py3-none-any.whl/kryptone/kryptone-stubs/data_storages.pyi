import dataclasses
import pathlib
from typing import (Any, Callable, Generic, List, Literal, Optional,
                    OrderedDict, Sequence, Type, TypeVar, Union, override)

import pyairtable
import redis
import requests
from requests.models import PreparedRequest

from kryptone.base import SiteCrawler

T = TypeVar('T')  # Generic

_Storage = TypeVar('_Storage', bound='BaseStorage')  # Storage

_Spider = TypeVar('_Spider', bound='SiteCrawler')  # Spider


def simple_list_adapter(
    data: List[Union[int, str, float]]
) -> List[List[str, int, float]]: ...


class BaseStorage:
    storage_class: Type[RedisStorage | FileStorage | ApiStorage] = ...
    storage_connection: Optional[RedisStorage | FileStorage | ApiStorage] = ...
    spider: Optional[SiteCrawler] = ...

    def __init__(self, *, spider: SiteCrawler = ...) -> None: ...

    def before_save(self, data: T) -> T: ...
    def initialize(self) -> bool: ...

    async def has(self, key: str) -> bool: ...

    async def get(
        self,
        key: str
    ) -> T: ...

    async def save(
        self,
        key: str,
        data: T,
        adapt_list: bool = ...,
        **kwargs
    ) -> bool: ...

    async def save_or_create(
        self,
        key: str,
        data: T
    ) -> bool: ...


@dataclasses.dataclass
class File:
    path: pathlib.Path

    def __eq__(self, value) -> bool: ...

    @property
    def is_json(self) -> bool: ...

    @property
    def is_csv(self) -> bool: ...

    @property
    def is_image(self) -> bool: ...

    def has(self, key: str) -> bool: ...

    def get(
        self,
        key: str
    ) -> Union[dict, list, bytes]: ...

    def save(
        self,
        key: str,
        data: Union[dict, list, bytes],
        adapt_list: bool = Literal[False],
        **kwargs
    ) -> None: ...


class FileStorage(BaseStorage, BaseStorage[_Storage]):
    storage: OrderedDict[str, File] = ...
    storage_path: Union[str, pathlib.Path] = ...
    csv_adapters: List[Callable[[Sequence[T], T]]]
    ignore_images: bool = ...

    def __init__(
        self,
        *,
        spider: Optional[SiteCrawler] = ...,
        storage_path: Union[str, pathlib.Path] = ...
    ) -> None: ...

    def __repr__(self) -> str: ...

    @override
    def initialize(self) -> bool: ...

    @override
    def has(self, filename: str) -> bool: ...

    @override
    def get(self, filename: str) -> File: ...

    @override
    def save(self, filename: str, data: T) -> bool: ...

    def get_file(self, filename: str) -> File: ...


class RedisStorage(BaseStorage, Generic[_Storage]):
    storage_class: Type[redis.Redis] = ...
    storage_connection: redis.Redis = ...
    is_connected: bool = ...

    def __init__(self, *, spider: Optional[SiteCrawler] = ...) -> None: ...


class AirtableStorage(BaseStorage, Generic[_Storage]):
    storage_class: Type[pyairtable.Api] = ...
    storage_connection: pyairtable.Api = ...

    def __init__(self) -> None: ...


class ApiStorage(BaseStorage, Generic[_Storage]):
    session: requests.Session = ...
    get_endpoint: str = ...
    save_endpoint: str = ...

    @property
    def default_headers(self) -> dict[str, str]: ...

    def check(self, name: str, data: Any) -> None: ...

    def create_request(
        self, url: str,
        method: Literal['post'] = 'post',
        data: Any = None
    ) -> PreparedRequest: ...

    def get(self, data_name) -> None: ...

    def create(self, data_name, data) -> bool: ...

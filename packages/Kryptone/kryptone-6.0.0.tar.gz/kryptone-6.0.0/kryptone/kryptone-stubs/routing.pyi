from typing import Callable, List, OrderedDict, Self, Tuple, Union

from kryptone.base import SiteCrawler
from kryptone.utils.urls import URL


class Route:
    path: str = ...
    regex: str = ...
    name: str = ...
    function_name: str = ...
    matched_urls: list = ...

    def __init__(self: Self) -> None: ...
    def __repr__(self: Self) -> str: ...

    def __call__(
        self: Self,
        function_name: str,
        *,
        path: str = ...,
        regex: str = ...,
        name: str = ...
    ) -> Tuple[Self, Callable[[str, SiteCrawler], bool]]: ...


def route(
    function_name: str,
    *,
    path: str = ...,
    regex: str = ...,
    name: str = ...
) -> Route: ...


class Router:
    routes: OrderedDict[
        str, 
        Callable[
            [str, SiteCrawler], 
            bool
        ]
    ] = ...

    def __init__(self: Self, routes: List[Route]) -> None: ...
    def __repr__(self: Self) -> str: ...

    @property
    def has_routes(self) -> bool: ...

    def resolve(
        self, current_url: Union[str, URL],
        spider_instance: SiteCrawler
    ) -> None: ...

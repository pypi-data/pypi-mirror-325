from typing import Any, Callable, Iterable, Optional, TypeVar

T = TypeVar("T")

def distinct(
    iterable: Iterable[T], key: Optional[Callable[[T], Any]] = None
) -> Iterable[T]: ...
def deep_merge_dicts(*dicts: dict[str, Any]) -> dict[str, Any]: ...
def partition(
    iterable: Iterable[T], predicate: Callable[[T], bool]
) -> tuple[list[T], list[T]]: ...

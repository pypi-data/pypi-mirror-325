from typing import Literal  # noqa: I001


def vercmp(a: str, b: str, silent: Literal[0, 1] = ...) -> int | None:
    ...


def catpkgsplit(
        s: str,
        silent: Literal[0, 1] = ...,
        eapi: str | None = ...
) -> tuple[str, str] | tuple[str, str, str] | tuple[str, str, str, str]:
    ...

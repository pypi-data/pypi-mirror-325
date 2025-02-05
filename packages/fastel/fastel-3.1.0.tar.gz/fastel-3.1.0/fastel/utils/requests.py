from functools import wraps
from typing import Any, Callable, Dict, TypeVar, cast

import requests as _requests
from starlette.datastructures import FormData

FuncT = TypeVar("FuncT", bound=Callable[..., Any])
WrapT = TypeVar("WrapT", bound=Callable[..., Any])


def log_all(action: str) -> WrapT:
    def inner(fn: FuncT) -> FuncT:
        @wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                url: str = args[0]
            except IndexError:
                url = kwargs["url"]

            json = kwargs.get("json", None)
            data = kwargs.get("data", None)
            print("[REQ]", action, f"url={url}", f"json={json}", f"data={data}")
            return fn(*args, **kwargs)

        return cast(FuncT, wrapper)

    return cast(WrapT, inner)


@log_all("get")  # type: ignore
def get(*args: Any, **kwargs: Any) -> Any:
    return _requests.get(*args, **kwargs)


@log_all("post")  # type: ignore
def post(*args: Any, **kwargs: Any) -> Any:
    return _requests.post(*args, **kwargs)


@log_all("put")  # type: ignore
def put(*args: Any, **kwargs: Any) -> Any:
    return _requests.put(*args, **kwargs)


@log_all("delete")  # type: ignore
def delete(*args: Any, **kwargs: Any) -> Any:
    return _requests.delete(*args, **kwargs)


def parse_formdata(formdata: FormData) -> Dict[str, Any]:
    parsed = {}
    for key in formdata.keys():
        parsed[key] = formdata.get(key)

    return parsed

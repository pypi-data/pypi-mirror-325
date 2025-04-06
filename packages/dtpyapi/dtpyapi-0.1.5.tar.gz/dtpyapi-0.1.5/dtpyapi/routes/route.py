from enum import Enum
from functools import wraps
from typing import Callable, List, Optional, Type, Any, Dict
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from .authentication import Auth, auth_data_class_to_dependency
from .response import (
    return_direct_file_response,
    return_json_response,
    return_file_response,
)


class ResponseType(Enum):
    JSON = "json"
    DIRECT_FILE = "direct_file"
    FILE = "file"
    CUSTOM = "custom"


class RouteMethod(Enum):
    GET = "GET"
    PUT = "PUT"
    POST = "POST"
    DELETE = "DELETE"
    PATCH = "PATCH"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"
    TRACE = "TRACE"
    CONNECT = "CONNECT"


class Route:
    def __init__(
        self,
        path: str,
        method: RouteMethod,
        handler: Callable,
        authentications: list[Auth] = None,
        response_type: ResponseType = ResponseType.JSON,
        response_model: Optional[Type[BaseModel]] = None,
        status_code: int = 200,
        dependencies: List[Any] = None,
        wrapper_kwargs: Dict[str, Any] = None,
        name: Optional[str] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        tags: Optional[List[str]] = None,
        response_description: str = "Successful Response",
        responses: Optional[Dict[int, Dict[str, Any]]] = None,
        deprecated: bool = False,
        operation_id: Optional[str] = None,
        include_in_schema: bool = True,
        response_class: Optional[Type[Any]] = JSONResponse,
        response_model_exclude_unset: bool = False,
        response_model_exclude_defaults: bool = False,
        response_model_exclude_none: bool = False,
        response_model_by_alias: bool = True,
    ):
        """
        Initialize a Route instance and create a wrapped handler.
        """
        dependencies = dependencies or []
        for authentication in (authentications or []):
            dependencies.extend(auth_data_class_to_dependency(authentication))

        self.dependencies = dependencies

        self.path = path
        self.method = method
        self.handler = handler
        self.response_type = response_type
        self.response_model = response_model
        self.status_code = status_code
        self.wrapper_kwargs = wrapper_kwargs or {}
        self.name = name
        self.summary = summary
        self.description = description
        self.tags = tags
        self.response_description = response_description
        self.responses = responses
        self.deprecated = deprecated
        self.operation_id = operation_id
        self.include_in_schema = include_in_schema
        self.response_class = response_class
        self.response_model_exclude_unset = response_model_exclude_unset
        self.response_model_exclude_defaults = response_model_exclude_defaults
        self.response_model_exclude_none = response_model_exclude_none
        self.response_model_by_alias = response_model_by_alias

    @staticmethod
    def is_async_callable(func: Callable) -> bool:
        return callable(func) and hasattr(func, "__await__")

    def wrapped_handler(self) -> Callable:
        """
        Create and return a wrapped handler based on the response type.
        """
        is_async = self.is_async_callable(self.handler)

        def wrap_function(wrapped_func: Callable) -> Callable:
            if self.response_type == ResponseType.JSON:
                @wraps(wrapped_func)
                async def async_wrapper(*args, **kwargs):
                    result = await wrapped_func(*args, **kwargs)
                    return return_json_response(data=result, status_code=self.status_code, **self.wrapper_kwargs)

                @wraps(wrapped_func)
                def sync_wrapper(*args, **kwargs):
                    result = wrapped_func(*args, **kwargs)
                    return return_json_response(data=result, status_code=self.status_code, **self.wrapper_kwargs)

                return async_wrapper if is_async else sync_wrapper

            elif self.response_type == ResponseType.DIRECT_FILE:
                @wraps(wrapped_func)
                async def async_wrapper(*args, **kwargs):
                    result = await wrapped_func(*args, **kwargs)
                    return return_direct_file_response(data=result, status_code=self.status_code, **self.wrapper_kwargs)

                @wraps(wrapped_func)
                def sync_wrapper(*args, **kwargs):
                    result = wrapped_func(*args, **kwargs)
                    return return_direct_file_response(data=result, status_code=self.status_code, **self.wrapper_kwargs)

                return async_wrapper if is_async else sync_wrapper

            elif self.response_type == ResponseType.FILE:
                @wraps(wrapped_func)
                async def async_wrapper(*args, **kwargs):
                    result = await wrapped_func(*args, **kwargs)
                    return return_file_response(data=result, status_code=self.status_code, **self.wrapper_kwargs)

                @wraps(wrapped_func)
                def sync_wrapper(*args, **kwargs):
                    result = wrapped_func(*args, **kwargs)
                    return return_file_response(data=result, status_code=self.status_code, **self.wrapper_kwargs)

                return async_wrapper if is_async else sync_wrapper

            elif self.response_type == ResponseType.CUSTOM:
                @wraps(wrapped_func)
                async def async_wrapper(*args, **kwargs):
                    return await wrapped_func(*args, **kwargs)

                @wraps(wrapped_func)
                def sync_wrapper(*args, **kwargs):
                    return wrapped_func(*args, **kwargs)

                return async_wrapper if is_async else sync_wrapper

            else:
                raise ValueError(f"Unsupported response type: {self.response_type}")

        return wrap_function(self.handler)

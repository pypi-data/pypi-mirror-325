import inspect
from copy import deepcopy
from functools import wraps
from typing import Callable, get_type_hints

from pydantic import ConfigDict, TypeAdapter

from chat2edit.execution.exceptions import FeedbackException
from chat2edit.execution.feedbacks import (
    IgnoredReturnValueFeedback,
    InvalidParameterTypeFeedback,
    UnexpectedErrorFeedback,
)
from chat2edit.execution.signaling import set_response
from chat2edit.models import Error
from chat2edit.prompting.stubbing.decorators import (
    exclude_this_decorator,
    exclude_this_decorator_factory,
)
from chat2edit.utils.repr import anno_repr


@exclude_this_decorator
def feedback_invalid_parameter_type(func: Callable):
    def validate_args(*args, **kwargs) -> None:
        signature = inspect.signature(func)
        bound_args = signature.bind(*args, **kwargs)
        bound_args.apply_defaults()
        hints = get_type_hints(func)

        for param_name, param_value in bound_args.arguments.items():
            param_anno = hints.get(param_name)

            if not param_anno:
                continue

            try:
                config = ConfigDict(arbitrary_types_allowed=True)
                adaptor = TypeAdapter(param_anno, config=config)
            except:
                adaptor = TypeAdapter(param_anno)

            try:
                adaptor.validate_python(param_value)
            except:
                feedback = InvalidParameterTypeFeedback(
                    function=func.__name__,
                    parameter=param_name,
                    expected_type=anno_repr(param_anno),
                    received_type=type(param_value).__name__,
                )
                raise FeedbackException(feedback)

    @wraps(func)
    def wrapper(*args, **kwargs):
        validate_args(*args, **kwargs)
        return func(*args, **kwargs)

    @wraps(func)
    async def async_wrapper(*args, **kwargs):
        validate_args(*args, **kwargs)
        return await func(*args, **kwargs)

    return async_wrapper if inspect.iscoroutinefunction(func) else wrapper


@exclude_this_decorator
def feedback_ignored_return_value(func: Callable):
    def check_caller_frame() -> None:
        caller_frame = inspect.currentframe().f_back.f_back
        instructions = list(inspect.getframeinfo(caller_frame).code_context or [])

        if not any(" = " in line for line in instructions):
            feedback = IgnoredReturnValueFeedback(
                function=func.__name__,
                value_type=anno_repr(get_type_hints(func).get("return")),
            )
            raise FeedbackException(feedback)

    @wraps(func)
    def wrapper(*args, **kwargs):
        check_caller_frame()
        return func(*args, **kwargs)

    @wraps(func)
    async def async_wrapper(*args, **kwargs):
        check_caller_frame()
        return await func(*args, **kwargs)

    return async_wrapper if inspect.iscoroutinefunction(func) else wrapper


@exclude_this_decorator
def feedback_unexpected_error(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FeedbackException as e:
            raise e
        except Exception as e:
            error = Error.from_exception(e)
            feedback = UnexpectedErrorFeedback(function=func.__name__, error=error)
            raise FeedbackException(feedback)

    @wraps(func)
    async def async_wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except FeedbackException as e:
            raise e
        except Exception as e:
            error = Error.from_exception(e)
            feedback = UnexpectedErrorFeedback(function=func.__name__, error=error)
            raise FeedbackException(feedback)

    return async_wrapper if inspect.iscoroutinefunction(func) else wrapper


@exclude_this_decorator_factory
def deepcopy_parameter(param: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        def check_and_transform_args_kwargs(args, kwargs):
            params = func.__code__.co_varnames[: func.__code__.co_argcount]

            if param in params:
                index = params.index(param)
                if index < len(args):
                    args = tuple(
                        deepcopy(arg) if i == index else arg
                        for i, arg in enumerate(args)
                    )

            if param in kwargs:
                kwargs[param] = deepcopy(kwargs[param])

            return args, kwargs

        @wraps(func)
        def wrapper(*args, **kwargs):
            args, kwargs = check_and_transform_args_kwargs(args, kwargs)
            return func(*args, **kwargs)

        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            args, kwargs = check_and_transform_args_kwargs(args, kwargs)
            return await func(*args, **kwargs)

        return async_wrapper if inspect.iscoroutinefunction(func) else wrapper

    return decorator


@exclude_this_decorator
def respond(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        set_response(response)
        return response

    @wraps(func)
    async def async_wrapper(*args, **kwargs):
        response = await func(*args, **kwargs)
        set_response(response)
        return response

    return async_wrapper if inspect.iscoroutinefunction(func) else wrapper

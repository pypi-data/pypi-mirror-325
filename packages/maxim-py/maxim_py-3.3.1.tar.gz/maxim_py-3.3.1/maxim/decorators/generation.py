import asyncio
import logging
from contextvars import ContextVar
from functools import wraps
from typing import Callable, Dict, List, Optional
from uuid import uuid4

from ..logger.components.generation import Generation, GenerationConfig
from ..logger.logger import Logger
from .span import current_span
from .trace import current_logger, current_trace

_generation_ctx_var: ContextVar[Optional[Generation]] = ContextVar(
    "maxim_ctx_generation", default=None
)


def current_generation() -> Optional[Generation]:
    return _generation_ctx_var.get()


def generation(
    logger: Optional[Logger] = None,
    id: Optional[Callable] or Optional[str] = None,
    name: Optional[str] = None,
    maxim_prompt_id: Optional[str] = None,
    tags: Optional[Dict[str, str]] = None,
    evaluators: Optional[List[str]] = None,
    evaluator_variables: Optional[Dict[str, str]] = None,
):
    def decorator(func):
        if asyncio.iscoroutinefunction(func):

            @wraps(func)
            async def wrapper(*args, **kwargs):
                # First check if the logger is available
                maxim_logger = logger
                if maxim_logger is None:
                    if current_logger() is None:
                        raise ValueError(
                            "[MaximSDK]: no logger found. either call this function from a @trace decorated function or pass a logger"
                        )
                    maxim_logger = current_logger()
                if current_span() is None and current_trace() is None:
                    if maxim_logger.raise_exceptions:
                        raise ValueError(
                            "[MaximSDK]: no trace or span found. either call this function from a @trace or @span decorated function"
                        )
                    else:
                        logging.warning(
                            "[MaximSDK]: no trace or span found. either call this function from a @trace or @span decorated function"
                        )
                actual_generation_id = id() if callable(id) else id
                if actual_generation_id is None:
                    actual_generation_id = str(uuid4())
                generation_config = GenerationConfig(
                    id=actual_generation_id,
                    name=name,
                    maxim_prompt_id=maxim_prompt_id,
                    tags=tags,
                )
                generation: Generation
                if current_span() is not None:
                    generation = current_span().generation(config=generation_config)
                elif current_trace() is not None:
                    generation = current_trace().generation(config=generation_config)
                if evaluators is not None:
                    generation.attach_evaluators(evaluators)
                if evaluator_variables is not None:
                    generation.with_variables(evaluators, evaluator_variables)
                token = _generation_ctx_var.set(generation)
                try:
                    return await func(*args, **kwargs)
                finally:
                    generation.end()
                    _generation_ctx_var.reset(token)

        else:

            @wraps(func)
            def wrapper(*args, **kwargs):
                # First check if the logger is available
                maxim_logger = logger
                if maxim_logger is None:
                    if current_logger() is None:
                        raise ValueError(
                            "[MaximSDK]: no logger found. either call this function from a @trace decorated function or pass a logger"
                        )
                    maxim_logger = current_logger()
                if current_span() is None and current_trace() is None:
                    if maxim_logger.raise_exceptions:
                        raise ValueError(
                            "[MaximSDK]: no trace or span found. either call this function from a @trace or @span decorated function"
                        )
                    else:
                        logging.warning(
                            "[MaximSDK]: no trace or span found. either call this function from a @trace or @span decorated function"
                        )
                actual_generation_id = id() if callable(id) else id
                if actual_generation_id is None:
                    actual_generation_id = str(uuid4())
                generation_config = GenerationConfig(
                    id=actual_generation_id,
                    name=name,
                    maxim_prompt_id=maxim_prompt_id,
                    tags=tags,
                )
                generation: Generation
                if current_span() is not None:
                    generation = current_span().generation(config=generation_config)
                elif current_trace() is not None:
                    generation = current_trace().generation(config=generation_config)
                token = _generation_ctx_var.set(generation)
                try:
                    return func(*args, **kwargs)
                finally:
                    generation.end()
                    _generation_ctx_var.reset(token)

        return wrapper

    return decorator

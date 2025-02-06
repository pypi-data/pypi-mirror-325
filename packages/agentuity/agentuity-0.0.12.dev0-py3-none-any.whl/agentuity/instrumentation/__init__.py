import os
import logging
from abc import ABC, abstractmethod
from typing import Any
from wrapt import wrap_function_wrapper
import json

logger = logging.getLogger(__name__)
log_level = os.getenv("LOG_LEVEL", "").upper()
numeric_level = 0
if log_level != "":
    # Convert the string to a logging level
    numeric_level = getattr(logging, log_level, None)
    logger.setLevel(level=numeric_level)


class BaseInstrumentation(ABC):
    _instance = None
    _is_instrumented_by_agentuity = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    @property
    def is_instrumented_by_agentuity(self):
        return self._is_instrumented_by_agentuity

    @abstractmethod
    def _instrument(self, **kwargs: Any):
        pass

    def _uninstrument(self, **kwargs: Any):
        pass

    def instrument(self, **kwargs: Any):
        """Instrument the library"""
        if self._is_instrumented_by_agentuity:
            logger.warning("Attempting to instrument while already instrumented")
            return None
        result = self._instrument(**kwargs)
        self._is_instrumented_by_agentuity = True
        return result

    def uninstrument(self, **kwargs: Any):
        """Uninstrument	the library"""
        if self._is_instrumented_by_agentuity:
            result = self._uninstrument(**kwargs)
            self._is_instrumented_by_agentuity = False
            return result

        logger.warning("Attempting to uninstrument while already uninstrumented")

        return None

    def _wrap(self, module, fn, before=None, after=None):
        def wrapper(wrapped, instance, args, kwargs):
            if before is not None:
                before(kwargs)
            response = wrapped(*args, **kwargs)
            if after is not None:
                after(kwargs, response)
            return response

        wrap_function_wrapper(module, fn, wrapper)
        return wrapper


def is_jsonable(x):
    try:
        json.dumps(x)
        return True
    except:
        return False


def getAgentuityLogger(name):
    logger = logging.getLogger(name)
    logger.setLevel(level=numeric_level)
    return logger


__all__ = ["BaseInstrumentor", "is_jsonable", "getAgentuityLogger"]

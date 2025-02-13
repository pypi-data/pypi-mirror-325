"""Base interceptor class"""

from abc import ABC, abstractmethod


class BaseInterceptor(ABC):
    """Base interceptor class"""

    def __init__(
            self,
            *args,
            port: int | None = None,
            **kwargs,
        ) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def start(self):
        """Start the interceptor"""
        pass

    @abstractmethod
    def stop(self):
        """Stop the interceptor"""
        pass
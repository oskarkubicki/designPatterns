from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Returning a handler from here will let us link handlers in a
        # convenient way like this:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


class AdditionHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request.typeof == 'addition':
            return "addition result is " + str(request.a + request.b)
        else:
            return super().handle(request)


class SubtractionHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request.typeof == 'subtraction':
            return 'subtraction result ' + str(request.a - request.b)
        else:
            super().handle(request)


class DivisionHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request.typeof == 'division':
            return 'Division result ' + str(request.a / request.b)
        else:
            super().handle(request)


class MultiplicationHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request.typeof == 'multiplication':
            return 'Multiplication result ' + str(request.a * request.b)
        else:
            super().handle(request)


class Request:
    def __init__(self, typeof, a, b):
        self.typeof = typeof
        self.a = a
        self.b = b

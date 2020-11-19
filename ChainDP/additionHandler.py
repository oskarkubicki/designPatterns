import AbstractHandler
from typing import Any


class additionHandler(AbstractHandler):
    def handle(self, request: Any):
        if request.type =='addition':
            return request.a+request.b
        else:
            return super().handle(request)

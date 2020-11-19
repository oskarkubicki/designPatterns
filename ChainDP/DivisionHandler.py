import AbstractHandler
from typing import Any


class DivisionHandler(AbstractHandler):
    def handle(self,request: Any):
        if request.type == 'division':
            return request.a/request.b
        else:
            return super(DivisionHandler, self).handle()

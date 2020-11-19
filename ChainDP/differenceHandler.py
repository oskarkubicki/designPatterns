import AbstractHandler
from typing import Any


class DifferenceHandler(AbstractHandler):
    def handle(self,request: Any):
        if request.type == 'division':
            return request.a/request.b
        else:
            return super(DifferenceHandler, self).handle()
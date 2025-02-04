import logging

from starlette.responses import JSONResponse
from starlette.types import ASGIApp, Receive, Scope, Send

from dbox.silos.errors import AppError

log = logging.getLogger(__name__)


class ErrorHandlerMiddleware:
    def __init__(self, app: ASGIApp):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] == "http":
            path = scope["path"]
            try:
                return await self.app(scope, receive, send)
            except AppError as e:
                log.error(e)
                res = JSONResponse({"error": {"message": e.get_message()}}, status_code=500)
                return await res(scope, receive, send)
            except Exception:
                log.exception("unknown error %s", path)
                res = JSONResponse({"error": {"messsage": "????"}}, status_code=500)
                return await res(scope, receive, send)
        else:
            await self.app(scope, receive, send)

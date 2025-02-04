import logging
from functools import cached_property

from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.types import ASGIApp, Receive, Scope, Send

from dbox.ctx import set_context

log = logging.getLogger(__name__)


class SecretAuthMiddleware:
    def __init__(
        self,
        app: ASGIApp,
    ):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            return await self.app(scope, receive, send)
        request = Request(scope, receive)
        # todo: take from scope directly
        secret = request.headers.get("x-secret")
        res = self.app
        username: str = None
        if secret is not None:
            if secret == "du@n123bon":
                username = "admin"
            else:
                res = JSONResponse({"error": {"message": "Vui lòng đăng nhập"}}, status_code=401)
        else:
            pass
        with set_context(username=username):
            await res(scope, receive, send)

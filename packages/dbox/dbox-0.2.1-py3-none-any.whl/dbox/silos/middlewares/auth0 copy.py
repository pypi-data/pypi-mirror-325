import logging
from functools import cached_property

import jose
from jose.jwt import decode
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.types import ASGIApp, Receive, Scope, Send

from dbox.ctx import set_context

log = logging.getLogger(__name__)


class JwtAuthMiddleware:
    def __init__(
        self,
        app: ASGIApp,
        audience: str = None,
        white_list=(),
        username_field="username",
        jwks=None,
        jwks_url=None,
    ):
        self.app = app
        self._jwks = jwks
        self._jwks_url = jwks_url
        self.audience = audience
        self.white_list = white_list
        self.username_field = username_field

    @cached_property
    def session(self):
        from requests_cache import CachedSession

        return CachedSession(backend="memory")

    @property
    def jwks(self):
        if self._jwks:
            return self._jwks
        return self.session.get(self._jwks_url).json()

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            return await self.app(scope, receive, send)
        request = Request(scope, receive)
        # todo: take from scope directly
        if request.url.path in self.white_list:
            await self.app(scope, receive, send)
            return
        bearer = request.headers.get("authorization")
        res = self.app
        username: str = None
        if bearer and bearer.lower().startswith("bearer "):
            try:
                token = bearer.split(" ")[1]
                # try cognito first
                options = {}
                if not self.audience:
                    options["verify_aud"] = False
                payload = decode(token, self.jwks, options=options, audience=self.audience)
                if self.audience:
                    assert payload["aud"] == self.audience
                username = payload[self.username_field]
            except jose.exceptions.ExpiredSignatureError:
                log.error("token expired")
                res = JSONResponse(
                    {"error": {"message": "Phiên hết hạn. Vui lòng logout và đăng nhập lại"}},
                    status_code=401,
                )
            except Exception:
                log.error("verify token failed", exc_info=True)
                res = JSONResponse({"error": {"message": "Vui lòng đăng nhập"}}, status_code=401)
        else:
            pass

            if True:  # conf.DEV:
                username = "quynhlt"
        with set_context(username=username):
            await res(scope, receive, send)

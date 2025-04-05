import json
import logging
from datetime import date, datetime, timezone
from decimal import Decimal
from functools import wraps
from time import monotonic
from typing import List

import pendulum
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.routing import Route

from dbox.ctx import set_context, use_factory, use_key
from dbox.om.ctx import use_sql_context

log = logging.getLogger(__name__)
use_username = use_factory(str, key="username")


def now():
    return use_key("now", tpe=pendulum.DateTime)


def route(
    *,
    path: str,
    methods: List[str] = ["GET"],  # noqa
    use_db: bool = False,
    cache_response: bool = False,
    authenticated_only: bool = False,
    admin_only: bool = False,
):
    def decorator(func):
        func = ensure_response(func)

        @wraps(func)
        async def decorated_handler(request: Request):
            with set_context(now=pendulum.now(tz=pendulum.UTC)):
                # if authenticated_only and not use_username(None):
                #     return JSONResponse({"error": {"message": "Vui lòng đăng nhập"}}, status_code=401)
                # if cache_response:
                #     key = request.url.path
                #     if key in _CACHE:
                #         log.debug("Serving %s from cache", key)
                #         return _CACHE[key]
                if admin_only:
                    if use_username(None) != "admin":
                        return JSONResponse({"error": {"message": "Vui lòng đăng nhập"}}, status_code=401)
                if use_db:
                    ctx = use_sql_context()
                    async with ctx.use_db():
                        res = await func(request)
                else:
                    res: Response = await func(request)
                return res

        return Route(path, decorated_handler, methods=methods)

    return decorator


def default_json_encoder(obj):
    if isinstance(obj, datetime):
        return obj.astimezone(tz=timezone.utc).isoformat().replace("+00:00", "Z")
    elif isinstance(obj, Decimal):
        return str(obj.normalize())
    elif isinstance(obj, date):
        return obj.isoformat()
    elif isinstance(obj, BaseModel):
        return obj.model_dump()
    else:
        return str(obj)


class AppResponse(JSONResponse):
    media_type = "application/json"

    def render(self, content):
        try:
            return json.dumps(
                content,
                ensure_ascii=False,
                allow_nan=False,
                indent=None,
                separators=(",", ":"),
                default=default_json_encoder,
            ).encode("utf-8")
        except Exception:
            log.exception("failed to dump %s", content)
            self.status_code = 500
            return r'{"error": {"message": "Có lỗi xảy ra"}}'.encode("utf-8")


def ensure_response(func):
    @wraps(func)
    async def wrapper(request: Request):
        res = await func(request)
        if not isinstance(res, Response):
            res = AppResponse(content=res)
        return res

    return wrapper

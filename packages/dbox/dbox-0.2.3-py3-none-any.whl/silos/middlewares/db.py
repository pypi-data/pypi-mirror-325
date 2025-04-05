import logging

from psycopg_pool import AsyncConnectionPool
from starlette.types import ASGIApp, Receive, Scope, Send

from dbox.om import SqlContext
from silos.conf import config

log = logging.getLogger(__name__)


class DbMiddleware:
    """Lazily create a new sql alchemy session"""

    def __init__(self, app: ASGIApp):
        self.app = app
        self._pool = AsyncConnectionPool(conninfo=config.conninfo, min_size=1, max_size=8, open=False, timeout=5)

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] == "http":
            try:
                with SqlContext(pool=self._pool):
                    await self.app(scope, receive, send)
            except Exception:
                raise

import logging
from time import monotonic

import pendulum
from starlette.types import ASGIApp, Receive, Scope, Send

from dbox.ctx import set_context, use_factory

log = logging.getLogger(__name__)


class TimingMiddleware:
    """Lazily create a new sql alchemy session"""

    def __init__(self, app: ASGIApp):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        start = monotonic()

        def wrapped_send(message):
            log.debug("Sending %s", message)
            type = message["type"]
            if type == "http.response.start":
                end = monotonic()
                # when we start sending the response, we can calculate the duration
                duration_seconds = end - start
                if duration_seconds > 5:
                    log.warning("Request took %.3fs", duration_seconds)
                if headers := message.get("headers"):
                    headers.append((b"X-Response-Time-Ms", f"{duration_seconds * 1000:.3f}".encode("utf-8")))
            return send(message)

        with set_context(now=pendulum.now(tz=pendulum.UTC)):
            await self.app(scope, receive, wrapped_send)


use_now = use_factory(pendulum.DateTime, key="now")

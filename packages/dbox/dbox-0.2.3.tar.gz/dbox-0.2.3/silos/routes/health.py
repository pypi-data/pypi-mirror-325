import logging

from starlette.requests import Request

from dbox.om import use_sql_context

from .utils import route

log = logging.getLogger(__name__)


@route(path="/healthz", methods=["GET"], use_db=True)
async def heatlhz(request):
    ctx = use_sql_context()
    server_info = await ctx.run_query(query="select version() as server_info")
    return {"status": "ok", **server_info}


routes = [heatlhz]

import json
from pathlib import Path

from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from starlette.routing import Mount, Route

from dbox.logging.colored import setup_colored_logging
from silos.middlewares import DbMiddleware, ErrorHandlerMiddleware, SecretAuthMiddleware, TimingMiddleware
from silos.routes.health import routes as health_routes
from silos.routes.upload import routes as upload_routes

DATA_DIR = Path("data")
setup_colored_logging()


async def store(request):
    key = request.path_params["key"]
    body = await request.json()
    with open(DATA_DIR / f"{key}.json", "w") as f:
        f.write(json.dumps(body, ensure_ascii=False))
    return JSONResponse({"message": "ok"})


routes = [
    Mount(
        "/dbox",
        routes=[
            *health_routes,
            Route("/store/{key}", store, methods=["POST"]),
            *upload_routes,
        ],
    )
]

app = Starlette(
    routes=routes,
    middleware=[
        Middleware(TimingMiddleware),
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_methods=["*"],
            allow_headers=["*"],
        ),
        Middleware(DbMiddleware),
        # we use this middleware to catch exceptions so that cors can work with internal errors
        Middleware(SecretAuthMiddleware),
        Middleware(ErrorHandlerMiddleware),
    ],
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("silos.app:app", host="127.0.0.1", port=10000, reload=True)

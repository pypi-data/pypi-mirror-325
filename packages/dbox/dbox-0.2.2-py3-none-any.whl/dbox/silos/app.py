import json
from pathlib import Path

from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from starlette.routing import Mount, Route

from dbox.silos.middlewares import ErrorHandlerMiddleware, SecretAuthMiddleware
from dbox.silos.routes.upload import routes as upload_routes

DATA_DIR = Path("data")


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
            Route("/healthz", lambda _: JSONResponse({"status": "ok"})),
            Route("/store/{key}", store, methods=["POST"]),
            *upload_routes,
        ],
    )
]

app = Starlette(
    routes=routes,
    middleware=[
        # Middleware(TimingMiddleware),
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_methods=["*"],
            allow_headers=["*"],
        ),
        # we use this middleware to catch exceptions so that cors can work with internal errors
        Middleware(SecretAuthMiddleware),
        Middleware(ErrorHandlerMiddleware),
    ],
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("dbox.silos.app:app", host="127.0.0.1", port=10000, reload=True)

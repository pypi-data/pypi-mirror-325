import logging
from typing import TYPE_CHECKING
from uuid import uuid4

import boto3
from botocore.config import Config
from starlette.requests import Request

if TYPE_CHECKING:
    from types_boto3_s3 import S3Client
from pendulum import UTC, now

from dbox.silos.conf import config
from dbox.silos.errors import fail

from .utils import route

log = logging.getLogger(__name__)
r2client: "S3Client" = boto3.client(
    "s3",
    endpoint_url=config.r2_endpoint_url,
    aws_access_key_id=config.r2_access_key_id,
    aws_secret_access_key=config.r2_secret_access_key,
    region_name="apac",
    config=Config(
        s3={"addressing_style": "virtual"},
        signature_version="v4",
        retries={"max_attempts": 3},
    ),
)


@route(path="/sign-upload-url", methods=["POST"], authenticated_only=True, admin_only=True)
async def sign_upload_url(request: Request):
    params = await request.json()
    name = params.get("name")
    if not name:
        fail("Missing name")
    name = params["name"][-30:]
    mime_type = params["mime_type"]
    size = params["size"]
    date = now(tz=UTC).date()

    final_key = f"{date.year}/{date.month}/{uuid4()}-{name}"

    # if size > 5 * 1024 * 1024:
    #     fail("File size too large")
    # if not mime_type.startswith("image/"):
    #     fail("Invalid file type")

    url = r2client.generate_presigned_url(
        ClientMethod="put_object",
        Params={
            "Bucket": config.r2_upload_bucket,
            "Key": final_key,
            "ContentType": mime_type,
            "ContentLength": size,
        },
    )

    return {"url": url, "key": final_key}


routes = [sign_upload_url]

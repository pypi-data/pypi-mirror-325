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


@route(path="/start-multipart-upload", methods=["POST"], authenticated_only=True, admin_only=True)
async def start_multipart_upload(request: Request):
    params = await request.json()
    name = params.get("name")
    if not name:
        fail("Missing name")
    name = params["name"][-30:]
    mime_type = params["mime_type"]
    size = params["size"]
    date = now(tz=UTC).date()

    final_key = f"{date.year}/{date.month}/{uuid4()}-{name}"

    response = r2client.create_multipart_upload(
        Bucket=config.r2_upload_bucket,
        Key=final_key,
        ContentType=mime_type,
    )

    upload_id = response["UploadId"]
    chunk_size = 100 * 1024 * 1024  # 100MB
    log.info("Created multipart upload %s", upload_id)
    num_parts = (size + chunk_size - 1) // chunk_size
    parts = []
    for i in range(num_parts):
        part_no = i + 1
        start = i * chunk_size
        end = min((i + 1) * chunk_size, size)
        url = r2client.generate_presigned_url(
            ClientMethod="upload_part",
            Params={
                "Bucket": config.r2_upload_bucket,
                "Key": final_key,
                "UploadId": upload_id,
                "PartNumber": part_no,
            },
            ExpiresIn=3600,
        )
        parts.append({"url": url, "start": start, "end": end, "part_no": part_no, "upload_id": upload_id})
    return {"parts": parts, "upload_id": upload_id, "key": final_key}


# r2client.upload_part
@route(path="/complete-multipart-upload", methods=["POST"], authenticated_only=True, admin_only=True)
async def complete_multipart_upload(request: Request):
    params = await request.json()
    # Bucket = params.get("Bucket")
    Key = params.get("Key")
    UploadId = params.get("UploadId")
    Parts = params.get("Parts")
    response = r2client.complete_multipart_upload(
        Bucket=config.r2_upload_bucket,
        Key=Key,
        UploadId=UploadId,
        MultipartUpload={"Parts": Parts},
    )
    return response


routes = [sign_upload_url, start_multipart_upload, complete_multipart_upload]

import logging
from typing import TYPE_CHECKING
from uuid import uuid4

import boto3
from botocore.config import Config
from pendulum import UTC, now
from starlette.requests import Request
from starlette.responses import RedirectResponse

from dbox.om import use_sql_context
from dbox.om.utils import get_one
from silos.conf import config
from silos.errors import fail
from silos.models import Upload, hash_password

from .utils import route

log = logging.getLogger(__name__)


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

    url = config.r2.generate_presigned_url(
        ClientMethod="put_object",
        Params={
            "Bucket": config.r2_upload_bucket,
            "Key": final_key,
            "ContentType": mime_type,
            "ContentLength": size,
        },
    )

    # store in database
    ctx = use_sql_context()
    upload = Upload.instance_create(data={"key": final_key, "password": params.get("password")}, ctx=ctx)
    await upload.db_create(ctx=ctx)
    await ctx.commit()

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

    response = config.r2.create_multipart_upload(
        Bucket=config.r2_upload_bucket,
        Key=final_key,
        ContentType=mime_type,
    )

    upload_id = response["UploadId"]
    chunk_size = 256 * 1024 * 1024  # 100MB
    log.info("Created multipart upload %s", upload_id)
    num_parts = (size + chunk_size - 1) // chunk_size
    parts = []
    for i in range(num_parts):
        part_no = i + 1
        start = i * chunk_size
        end = min((i + 1) * chunk_size, size)
        url = config.r2.generate_presigned_url(
            ClientMethod="upload_part",
            Params={
                "Bucket": config.r2_upload_bucket,
                "Key": final_key,
                "UploadId": upload_id,
                "PartNumber": part_no,
            },
            ExpiresIn=3600,
        )
        parts.append({"url": url, "start": start, "end": end, "part_no": part_no})

    # presign complete multipart upload
    complete_url = config.r2.generate_presigned_url(
        ClientMethod="complete_multipart_upload",
        Params={
            "Bucket": config.r2_upload_bucket,
            "Key": final_key,
            "UploadId": upload_id,
        },
        ExpiresIn=3600,
        HttpMethod="POST",
    )
    # presign abort multipart upload
    abort_url = config.r2.generate_presigned_url(
        ClientMethod="abort_multipart_upload",
        Params={
            "Bucket": config.r2_upload_bucket,
            "Key": final_key,
            "UploadId": upload_id,
        },
        ExpiresIn=3600,
        HttpMethod="DELETE",
    )

    # store in database
    ctx = use_sql_context()
    async with ctx.use_db():
        upload = Upload.instance_create(data={"key": final_key, "password": params.get("password")}, ctx=ctx)
        await upload.db_create(ctx=ctx)

    return {
        "key": final_key,
        "short_key": upload.short_key,
        "upload_id": upload_id,
        "parts": parts,
        "complete_url": complete_url,
        "abort_url": abort_url,
        "password_protected": upload.password is not None,
    }


@route(path="/download", methods=["POST"], authenticated_only=True, admin_only=True)
async def download_url(request: Request):
    params = await request.json()
    short_key = params.get("short_key")
    if not short_key:
        fail("Missing short_key")
    password = params.get("password")
    password = hash_password(password.encode()) if password else None
    ctx = use_sql_context()
    async with ctx.use_db():
        # upload = await get_one(Upload, )
        upload = await ctx.run_query(
            query="select * from upload where short_key = %(short_key)s", params={"short_key": short_key}
        )
    if not upload:
        fail("Upload not found", code=404)
    # print(upload)
    upload = Upload(**upload)
    if upload.password != password:
        print(upload.password, password)
        fail("Invalid password", code=403)
    if upload.expired_at and upload.expired_at < now().naive():
        fail("Upload expired", code=403)
    # all correct, generate presigned url
    url = config.r2.generate_presigned_url(
        ClientMethod="get_object",
        Params={
            "Bucket": config.r2_upload_bucket,
            "Key": upload.key,
        },
        ExpiresIn=3600,
    )
    return {"url": url}


# @route(path="/complete-multipart-upload", methods=["POST"], authenticated_only=True, admin_only=True)
# async def complete_multipart_upload(request: Request):
#     params = await request.json()
#     # Bucket = params.get("Bucket")
#     Key = params.get("Key")
#     UploadId = params.get("UploadId")
#     Parts = params.get("Parts")
#     response = config.r2.complete_multipart_upload(
#         Bucket=config.r2_upload_bucket,
#         Key=Key,
#         UploadId=UploadId,
#         MultipartUpload={"Parts": Parts},
#     )
#     return response


routes = [sign_upload_url, start_multipart_upload, download_url]

import os
from typing import TYPE_CHECKING

from attrs import Attribute, define, fields


@define(slots=False)
class _Config:
    r2_access_key_id: str = None
    r2_secret_access_key: str = None
    r2_endpoint_url: str = "https://755916c5f0af258bc5813685e4ba25a3.r2.cloudflarestorage.com"
    r2_upload_bucket: str = "a-bc-hdx"
    r2_temp_bucket: str = "a-bc-blackhole"

    secret: str = None

    database: str = "dbox"
    host: str = "localhost"
    port: str = "5432"
    user: str = "dbox"
    password: str = None

    @property
    def conninfo(self):
        return f"dbname={self.database} user={self.user} host={self.host} password={self.password}"

    @property
    def r2(self):
        if hasattr(self, "_r2"):
            return self._r2
        import boto3
        from botocore.config import Config

        if TYPE_CHECKING:
            from types_boto3_s3 import S3Client

        r2client: "S3Client" = boto3.client(
            "s3",
            endpoint_url=self.r2_endpoint_url,
            aws_access_key_id=self.r2_access_key_id,
            aws_secret_access_key=self.r2_secret_access_key,
            region_name="apac",
            config=Config(
                s3={"addressing_style": "virtual"},
                signature_version="v4",
                retries={"max_attempts": 3},
            ),
        )
        self._r2 = r2client
        return r2client

    def __attrs_post_init__(self):
        for field in fields(type(self)):
            field: Attribute
            env_name = field.name.upper()
            value = os.getenv("DBOX_" + env_name) or os.getenv(env_name)
            if value is not None:
                setattr(self, field.name, value)


config = _Config()

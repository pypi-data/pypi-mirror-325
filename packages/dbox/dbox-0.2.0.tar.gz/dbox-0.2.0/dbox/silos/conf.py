import os

from attrs import Attribute, define, fields


@define()
class Config:
    r2_access_key_id: str = None
    r2_secret_access_key: str = None
    r2_endpoint_url: str = "https://755916c5f0af258bc5813685e4ba25a3.r2.cloudflarestorage.com"
    r2_upload_bucket: str = "a-bc-hdx"

    def __attrs_post_init__(self):
        for field in fields(type(self)):
            field: Attribute
            env_name = field.name.upper()
            value = os.getenv(env_name)
            if value is not None:
                setattr(self, field.name, value)


config = Config()

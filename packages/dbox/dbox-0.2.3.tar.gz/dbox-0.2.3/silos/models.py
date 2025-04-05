import logging
import random
import string
from datetime import datetime, timedelta
from decimal import Decimal
from hashlib import scrypt
from typing import Annotated, Any, ClassVar, Dict, List, Optional

from pydantic import StringConstraints

from dbox.om import DModel, Omt, SqlContext
from silos.middlewares.timing import use_now

log = logging.getLogger(__name__)


class Upload(DModel):
    """
    create table upload (
        id serial primary key,
        key text not null,
        short_key text not null unique,
        password bytea,
        created_at timestamp not null,
        expired_at timestamp not null
    );
    """

    __tablename__: ClassVar[str] = "upload"

    id: Annotated[Optional[int], Omt(pk=True)] = None
    key: Optional[str] = None
    short_key: Annotated[Optional[str], Omt(system_column=True)] = None
    password: Optional[bytes] = None
    created_at: Optional[datetime] = None
    expired_at: Annotated[Optional[datetime], Omt(system_column=True)] = None

    @classmethod
    def instance_create(cls, data: Dict[str, Any], ctx: SqlContext | None = None):
        instance = super(Upload, cls).instance_create(data, ctx)
        instance.created_at = use_now()
        instance.expired_at = instance.created_at + timedelta(days=1)
        instance.short_key = random_string()
        if instance.password:
            instance.password = hash_password(instance.password)
        return instance


def random_string() -> str:
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=12))


def hash_password(password: bytes) -> bytes:
    return scrypt(password, salt=b"salt", n=2 << 10, r=8, p=1, dklen=8)

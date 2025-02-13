import binascii
from base64 import b64decode, b64encode
from typing import NamedTuple, Optional, Union

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.forms import model_to_dict
from graphql.type.scalars import serialize_id

Base64String = str

GLOBAL_ID_SECRET_KEY = getattr(settings, "GLOBAL_ID_SECRET_KEY", None)
if not GLOBAL_ID_SECRET_KEY:
    raise ImproperlyConfigured("GLOBAL_ID_SECRET_KEY는 반드시 설정되어야 합니다.")


class ResolvedGlobalId(NamedTuple):
    type: str
    id: str


def base64(s: str) -> Base64String:
    """Encode the string s using Base64."""
    b: bytes = s.encode("utf-8") if isinstance(s, str) else s
    return b64encode(b).decode("ascii")


def unbase64(s: Base64String) -> str:
    """Decode the string s using Base64."""
    try:
        b: bytes = s.encode("ascii") if isinstance(s, str) else s
    except UnicodeEncodeError:
        return ""
    try:
        return b64decode(b).decode("utf-8")
    except (binascii.Error, UnicodeDecodeError):
        return ""


def is_valid_base64(s: str) -> bool:
    try:
        return b64encode(b64decode(s)) == s.encode()
    except Exception:
        return False


def from_global_id(global_id: str) -> ResolvedGlobalId:
    """
    to_global_id로 생성된 "global ID"를 받아서
    이를 생성하는데 사용된 type name과 ID를 반환합니다.
    """
    if not is_valid_base64(global_id):
        raise ValueError("global_id가 유효하지 않습니다.")

    global_id = unbase64(global_id)
    split_global_id = global_id.split(":", 2)
    if split_global_id[-1] != GLOBAL_ID_SECRET_KEY:
        raise ValueError("secret key가 일치하지 않습니다.")

    return ResolvedGlobalId(*global_id.split(":", 2)[:2])


def to_global_id(type_: str, id_: Union[str, int]) -> str:
    """
    Takes a type name and an ID specific to that type name, and returns a
    "global ID" that is unique among all types.
    """
    return base64(f"{type_}:{serialize_id(id_)}:{GLOBAL_ID_SECRET_KEY}")


class BaseORMEnum(models.TextChoices):
    @classmethod
    def of(cls, value) -> Optional["BaseORMEnum"]:
        if value is None:
            return None

        for tag in cls:
            if tag.value == value:
                return tag
        return None


class BaseORMModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, help_text="생성일")
    modified_at = models.DateTimeField(auto_now=True, help_text="수정일")

    class Meta:
        abstract = True

    @property
    def created_ts(self) -> float:
        return self.created_at.timestamp() * 1e3

    @property
    def modified_ts(self):
        return self.modified_at.timestamp() * 1e3

    @classmethod
    def _check_global_id_type(cls, global_id: str):
        resolved_global_id = from_global_id(global_id)

        if resolved_global_id.type != cls.__name__:
            raise ValueError("global_id의 type이 일치하지 않습니다.")

        return resolved_global_id.id

    @classmethod
    def get_by_global_id(cls, global_id: str):
        _id = cls._check_global_id_type(global_id)

        return cls.objects.get(pk=_id)

    @classmethod
    def get_with_global_id(cls, global_id: str, **kwargs):
        _id = cls._check_global_id_type(global_id)

        return cls.objects.get(pk=_id, **kwargs)

    @classmethod
    def filter_by_global_id(cls, global_id: str, **kwargs):
        _id = cls._check_global_id_type(global_id)

        return cls.objects.filter(pk=_id, **kwargs)

    @classmethod
    def id_from_global_id(cls, global_id: str):
        return cls._check_global_id_type(global_id)

    @property
    def global_id(self) -> str:
        return to_global_id(self.__class__.__name__, self.pk)

    def to_dict(self):
        return {
            **model_to_dict(self),
            "global_id": self.global_id,
        }

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

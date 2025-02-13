from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import BaseORMModel


class User(AbstractUser, BaseORMModel):
    """
    사용자 모델
    """

    uid = models.CharField(
        _("Firebase UID"),
        primary_key=True,
        max_length=128,
        null=False,
        blank=False,
        editable=False,
    )

    email = models.EmailField(
        _("이메일 주소"),
        null=False,
        blank=False,
    )
    email_verified = models.BooleanField(
        _("이메일 인증 여부"),
        default=False,
    )
    provider_data = models.JSONField(
        _("제공 업체 데이터"),
        null=True,
        blank=True,
    )

    first_name = None
    last_name = None

    REQUIRED_FIELDS = ["email", "uid"]

    class Meta:
        db_table = "user"
        verbose_name = _("사용자")
        verbose_name_plural = _("사용자")
        indexes = [models.Index(fields=["email"], name="email_index")]

    def __str__(self):
        return f"<User: {self.email}>"

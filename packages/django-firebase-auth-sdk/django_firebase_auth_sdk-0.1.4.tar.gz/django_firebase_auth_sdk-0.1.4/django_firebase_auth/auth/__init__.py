from datetime import datetime, timezone

from asgiref.sync import sync_to_async
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, AnonymousUser
from firebase_admin import auth
from firebase_admin.auth import UserInfo, UserRecord

AUTHORIZATION_HEADER = getattr(
    settings,
    "AUTHORIZATION_HEADER",
    "Authorization",
)
AUTHORIZATION_HEADER_PREFIX = getattr(
    settings,
    "AUTHORIZATION_HEADER_PREFIX",
    "Bearer",
)
COOKIE_NAME = getattr(settings, "COOKIE_NAME", None)
AUTO_CREATE_USER = getattr(settings, "AUTO_CREATE_USER", False)


UserModel = get_user_model()


def is_valid_jwt(token):
    return len(token.split(".")) == 3


def timestamp_to_datetime(timestamp: int) -> datetime:
    return datetime.fromtimestamp(timestamp / 1000, tz=timezone.utc)


def provider_data_to_dict(provider_data: list[UserInfo]) -> dict:
    return [
        {
            "uid": p.uid,
            "email": p.email,
            "display_name": p.display_name,
            "phone_number": p.phone_number,
            "photo_url": p.photo_url,
            "provider_id": p.provider_id,
        }
        for p in provider_data
    ]


def create_user(user_record: UserRecord) -> AbstractBaseUser | None:
    if not AUTO_CREATE_USER:
        return None

    user, _ = UserModel.objects.update_or_create(
        uid=user_record.uid,
        defaults={
            "username": user_record.email,
            "password": make_password(f"{user_record.provider_id}:{user_record.uid}"),
            "email": user_record.email,
            "email_verified": user_record.email_verified,
            "date_joined": timestamp_to_datetime(user_record.user_metadata.creation_timestamp),
            "last_login": timestamp_to_datetime(user_record.user_metadata.last_sign_in_timestamp),
            "is_superuser": False,
            "is_staff": False,
            "provider_data": provider_data_to_dict(user_record.provider_data),
        },
    )

    return user


def get_user(request):
    # request에서 토큰 가져오기
    token = request.headers.get(AUTHORIZATION_HEADER)
    if COOKIE_NAME:
        token = token or request.COOKIES.get(COOKIE_NAME)

    if not token:
        return

    # 토큰 형식 검증
    token = token.replace(AUTHORIZATION_HEADER_PREFIX, "").strip()
    if not is_valid_jwt(token):
        return

    # 토큰 검증
    decoded_token = auth.verify_id_token(token)

    # Firebase에서 사용자 정보 조회
    user_record = auth.get_user(decoded_token["uid"])

    # DB에 사용자 정보 조회 또는 생성
    user = None
    try:
        # 사용자 정보 조회
        user = UserModel.objects.get(uid=user_record.uid)

        # 변경이 필요한 필드만 업데이트
        updates = {}

        if user.email_verified != user_record.email_verified:
            updates["email_verified"] = user_record.email_verified

        npd = provider_data_to_dict(user_record.provider_data)
        if user.provider_data != npd:
            updates["provider_data"] = npd

        nll = timestamp_to_datetime(user_record.user_metadata.last_sign_in_timestamp)
        if user.last_login != nll:
            updates["last_login"] = nll

        # 변경사항이 있을 때만 update() 호출
        if updates:
            UserModel.objects.filter(uid=user.uid).update(**updates)

        user.refresh_from_db()
    except UserModel.DoesNotExist:
        user = create_user(user_record)

    return user or AnonymousUser()


async def aget_user(request):
    """See get_user()."""
    return await sync_to_async(get_user)(request)

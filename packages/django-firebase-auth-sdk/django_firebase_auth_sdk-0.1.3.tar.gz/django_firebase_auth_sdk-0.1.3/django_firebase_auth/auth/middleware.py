from datetime import datetime, timezone
from typing import Type

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser
from django.utils.deprecation import MiddlewareMixin
from firebase_admin import auth
from firebase_admin.auth import UserInfo, UserRecord

# 설정 값 읽기
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
COOKIE_MAX_AGE = getattr(settings, "COOKIE_MAX_AGE", 3600)
COOKIE_HTTP_ONLY = getattr(settings, "COOKIE_HTTP_ONLY", True)
COOKIE_SECURE = getattr(settings, "COOKIE_SECURE", True)
COOKIE_SAMESITE = getattr(settings, "COOKIE_SAMESITE", "Lax")
AUTO_CREATE_USER = getattr(settings, "AUTO_CREATE_USER", False)


# 사용자 모델 타입 가져오기
UserModel: Type[AbstractBaseUser] = get_user_model()


def is_valid_jwt(token):
    return len(token.split(".")) == 3


class AuthenticationMiddleware(MiddlewareMixin):

    @staticmethod
    def timestamp_to_datetime(timestamp: int) -> datetime:
        return datetime.fromtimestamp(timestamp / 1000, tz=timezone.utc)

    @staticmethod
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

    def create_user(self, user_record: UserRecord) -> AbstractBaseUser | None:
        if not AUTO_CREATE_USER:
            return None

        user, _ = UserModel.objects.update_or_create(
            uid=user_record.uid,
            defaults={
                "username": user_record.email,
                "password": make_password(f"{user_record.provider_id}:{user_record.uid}"),
                "email": user_record.email,
                "email_verified": user_record.email_verified,
                "date_joined": self.timestamp_to_datetime(
                    user_record.user_metadata.creation_timestamp
                ),
                "last_login": self.timestamp_to_datetime(
                    user_record.user_metadata.last_sign_in_timestamp
                ),
                "is_superuser": False,
                "is_staff": False,
                "provider_data": self.provider_data_to_dict(user_record.provider_data),
            },
        )

        return user

    def process_request(self, request):
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

            npd = self.provider_data_to_dict(user_record.provider_data)
            if user.provider_data != npd:
                updates["provider_data"] = npd

            nll = self.timestamp_to_datetime(user_record.user_metadata.last_sign_in_timestamp)
            if user.last_login != nll:
                updates["last_login"] = nll

            # 변경사항이 있을 때만 update() 호출
            if updates:
                UserModel.objects.filter(uid=user.uid).update(**updates)

            user.refresh_from_db()
        except UserModel.DoesNotExist:
            user = self.create_user(user_record)

        if not user:
            return

        request.user = user
        request._user = user

    def process_response(self, request, response):
        token = request.headers.get(AUTHORIZATION_HEADER)
        if not token:
            return response
        if not is_valid_jwt(token):
            return response

        # 쿠키에 토큰 설정
        if COOKIE_NAME:
            response.set_cookie(
                COOKIE_NAME,  # 쿠키 이름
                token,  # 토큰 값
                max_age=COOKIE_MAX_AGE,  # 쿠키 유효 시간 (초 단위, 여기서는 1시간)
                httponly=COOKIE_HTTP_ONLY,
                secure=COOKIE_SECURE,
                samesite=COOKIE_SAMESITE,
            )
        return response

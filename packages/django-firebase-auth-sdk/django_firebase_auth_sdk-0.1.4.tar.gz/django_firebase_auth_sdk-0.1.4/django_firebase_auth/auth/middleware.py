from functools import partial

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser
from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject

from django_firebase_auth import auth

# 설정 값 읽기
AUTHORIZATION_HEADER = getattr(settings, "AUTHORIZATION_HEADER", "Authorization")

COOKIE_NAME = getattr(settings, "COOKIE_NAME", None)
COOKIE_MAX_AGE = getattr(settings, "COOKIE_MAX_AGE", 3600)
COOKIE_HTTP_ONLY = getattr(settings, "COOKIE_HTTP_ONLY", True)
COOKIE_SECURE = getattr(settings, "COOKIE_SECURE", True)
COOKIE_SAMESITE = getattr(settings, "COOKIE_SAMESITE", "Lax")


# 사용자 모델 타입 가져오기
UserModel: AbstractBaseUser = get_user_model()


def get_user(request):
    if not hasattr(request, "_cached_user"):
        request._cached_user = auth.get_user(request)
    return request._cached_user


async def auser(request):
    if not hasattr(request, "_acached_user"):
        request._acached_user = await auth.aget_user(request)
    return request._acached_user


class AuthenticationMiddleware(MiddlewareMixin):

    def process_request(self, request):
        request.user = SimpleLazyObject(lambda: get_user(request))
        request.auser = partial(auser, request)

    def process_response(self, request, response):
        token = request.headers.get(AUTHORIZATION_HEADER)
        if not token:
            return response
        if not auth.is_valid_jwt(token):
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

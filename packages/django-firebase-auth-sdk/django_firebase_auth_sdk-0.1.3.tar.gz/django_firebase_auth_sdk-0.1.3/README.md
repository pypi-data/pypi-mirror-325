# django-firebase-auth

 Quantit Django 프로젝트에서 Firebase Authentication을 쉽게 통합할 수 있는 패키지입니다.
 Client에서 Firebase에게서 발급 받은 token을 바탕으로 사용자를 인증하고, 사용자 정보를 동기화합니다.

## 특징

- Firebase ID 토큰 검증
- Django 사용자 자동 생성 및 동기화
- Global ID 지원하도록 BaseModel 클레스 제공

## Requirements

- Python ^3.12
- Django >=5.1, <6.0
- Firebase Admin SDK >=6.3, <7.0
- GraphQL Core >=3.1, <3.3

## 설치
GitHub에서 직접 설치:
```bash
# pip 사용
pip install git+https://github.com/Quantit-Github/django-firebase-auth.git

# poetry 사용
poetry add git+https://github.com/Quantit-Github/django-firebase-auth.git
```

## 사용 방법

### firebase admin sdk 설정(필수)
firebase admin sdk 설정이 필수적으로 필요합니다.
```python
# settings.py
import firebase_admin
from firebase_admin import credentials

// ... existing code ...

cred = credentials.Certificate(f"path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

// ... existing code ...
```

### 앱 추가하기
앱 설정 파일에 아래 내용을 추가합니다.
```python
# settings.py

// ... existing code ...

INSTALLED_APPS = [
    ...
    "django_firebase_auth",
    ...
]

// ... existing code ...
```

## middleware 설정
settings.py에 작성한 middleware를 등록합니다.
```python
# settings.py

// ... existing code ...

MIDDLEWARE = [
    ...
    "django_firebase_auth.auth.middleware.AuthenticationMiddleware",
    ...
]

// ... existing code ...
```

### User 모델 설정
```python
# settings.py

// ... existing code ...

AUTH_USER_MODEL = "django_firebase_auth.User"

// ... existing code ...
```

django_firebase_auth.User를 상속받은 커스텀 모델 역시 사용 가능합니다.
```python
# models.py

from django_firebase_auth.models import User

class CustomUser(User):
    pass
```

```python
# settings.py

// ... existing code ...

AUTH_USER_MODEL = "your_app.CustomUser"

// ... existing code ...
```

### 설정 옵션
아래와 같은 configure을 지원합니다.
```python
# settings.py

// ... existing code ...
GLOBAL_ID_SECRET_KEY = "your_secret_key" # 전역 ID 시크릿 키, 반드시 설정되어야 함(필수)

AUTHORIZATION_HEADER = "Authorization" # token이 포함된 헤더 이름, 기본값은 "Authorization"
AUTHORIZATION_HEADER_PREFIX = "Bearer" # token 앞에 붙는 접두사, 기본값은 "Bearer"

# 쿠키 설정
COOKIE_NAME = "firebase_auth_token" # 쿠키 이름, 기본값은 None. None일 경우 response에 쿠키를 추가하지 않음
COOKIE_MAX_AGE = 3600 # 쿠키 만료 시간, 기본값은 3600초(1시간)
COOKIE_HTTP_ONLY = True # 쿠키가 HTTP 전용인지 여부, 기본값은 True
COOKIE_SECURE = True # 쿠키가 HTTPS 전용인지 여부, 기본값은 True
COOKIE_SAMESITE = "Lax" # 쿠키의 SameSite 속성, 기본값은 "Lax"

# 사용자 자동 생성 여부
AUTO_CREATE_USER = True # 기본값은 False, 사용자 자동 생성 여부

// ... existing code ...
```

만일 AUTHORIZATION_HEADER를 따로 지정하시면서 CORS 설정이 되어 계시다면,
CORS_ALLOW_HEADERS에 아래 값을 추가해주세요.
```python
# settings.py

// ... existing code ...

CORS_ALLOW_HEADERS = [
    ...
    AUTHORIZATION_HEADER,
    ...
]

// ... existing code ...
```

## 사용자 생성 override
AuthenticationMiddleware에서 create_user 메서드를 override하여 사용자 생성 로직을 커스텀할 수 있습니다.
```python
# middleware.py
from django_firebase_auth.auth.middleware import AuthenticationMiddleware

// ... existing code ...


class CustomAuthenticationMiddleware(AuthenticationMiddleware):
    def create_user(self, user_record: UserRecord):
        ...

// ... existing code ...
```
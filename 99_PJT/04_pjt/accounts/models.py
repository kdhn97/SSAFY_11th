from django.db import models
# AbstractUser - 관리자 권한을 가지고 있는 User model을 구현하는 추상 기본클래스
from django.contrib.auth.models import AbstractUser

#  AbstractUser 클래스를 상속받는 커스텀 User 클래스 작성
class User(AbstractUser):
    pass
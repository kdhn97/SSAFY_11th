from django.db import models
from django.contrib.auth.models import AbstractUser

#  AbstractUser 클래스를 상속받는 커스텀 User 클래스 작성
class User(AbstractUser):
    pass
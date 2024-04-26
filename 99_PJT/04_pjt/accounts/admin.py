from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User # User model 대체하기

# 관리자 페이지 User 모델 생성
admin.site.register(User, UserAdmin)
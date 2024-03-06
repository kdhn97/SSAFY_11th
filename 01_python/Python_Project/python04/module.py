# core
# 모듈명과 똑같은 파일명을 쓰면 해당 파일의 함수 호출

# built-in
# 모듈 -> 함수 모아놓은 파일
import random
import question

# 3rd party library
import requests
from django.db.models import Model
from django.forms import ModelForm, forms
from django.contrib.auth.decorators import login_required

# print(random.sample(range(1,46),6))
print(question.my_sum(3, 5))

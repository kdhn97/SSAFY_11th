# UserCreationForm() - 회원 가입 시 사용자 입력 데이터를 받는 built-in ModelForm
from django.contrib.auth.forms import UserCreationForm
# UserChangeForm() - 회원정보 수정 시 사용자 입력 데이터를 받는 built-in ModelForm
from django.contrib.auth.forms import UserChangeForm
# get_user_model() - ‘현재 프로젝트에서 활성화된 사용자 모델’을 반환하는 함수
from django.contrib.auth import get_user_model
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')

class CustomUserChangeForm(UserChangeForm):
    # password = False
    password = forms.CharField(
        label = False,
        widget=forms.Textarea(
            attrs={
            'class': 'form-none'
            }
        )
    )
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')
            
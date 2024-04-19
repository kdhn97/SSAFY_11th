from django import forms
from .models import Board, Comment

# ModelForm - Model.py에 정의한 필드만 입력받고 싶다면
# Form - DB에 저장하지 않고 원하는 필드가 추가로 있다면

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('title', 'content', )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )
        
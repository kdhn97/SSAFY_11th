from django import forms
from .models import Movie

class MovieForm(forms.ModelForm): # ModelForm - 사용자 입력 데이터를 DB에 저장해야 할 때 ( 게시글 작성, 회원가입 )
    class Meta: # class Meta - ModelForm의 정보를 작성하는 곳
        model = Movie
        fields = '__all__' # 모든 속성 추가
        # exclude = ('title',) # title 필드가 보이지 않게
        
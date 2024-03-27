# articles/forms.py
from django import forms 
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__' # 모든 속성 추가
        # exclude = ('title',) # title 필드 보이지 않게
from .models import Keyword
from django import forms

class KeywordForm(forms.ModelForm):
    class Meta:
        model = Keyword
        fields = '__all__'
        labels = {
            'name': '키워드'
        }
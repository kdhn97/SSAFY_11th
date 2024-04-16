# 05_pjt : 김동현, 어지민

### Crawling
- 어려웠던 부분
  1. 저장 시 이미 저장되어 있는 키워드라면, 새로 생성하지 않고 검색 결과 개수를 변경
  2. 히스토그램 출력
  3. 필터링 - 저장 시 검색 기간(search_period)을 “year” 로 저장
   
- 해결
  - 크롤링 출력값 "검색결과 약 19,500,000개 (0.29초)"에서 개수만 출력한 방법 -> Trend.objects.create(name=keyword.name, result=int(crawling[7:end_idx].replace(',','')), search_period='all')
  - 이미지 데이터를 Base64 문자열로 변환 : image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
  - Trend.objects.filter(search_period='year')을 통하여 필터링

- 느낀 점
  - Views.py 작성에 어려움을 느끼기에 집중 복습 구간

### `ModelForm`에서 `label` 바꾸는 법
``` python
class KeywordForm(forms.ModelForm):
    class Meta:
        model = Keyword
        fields = '__all__'
        labels = {
            'name': '키워드'
        }
```

### 키워드 추가 - 'n'번째 키워드를 pk가 아니라 keyword의 개수로 하는법
- 변경 전
``` html
<!-- keyword.html -->
{% for keyword in keywords %}
    <p>{{ keyword.pk }}번째 키워드 - {{ keyword.name }}</p>
    <form action="{% url "keyword_delete" keyword.pk%}" method='POST'>
      {% csrf_token %}
      <input type="submit" value='삭제하기'>
    </form>
    <hr>
{% endfor %}  
```


- 변경 후
``` python 
# keyword view 함수 
keywords_dict = {}

for i in range(len(keywords)):
    keywords_dict[i+1] = keywords[i]
      
context = {
    'form': form,
    'keywords_dict': keywords_dict
}
return render(request, 'trends/keyword.html', context)
```
``` html
<!-- keyword.html -->
{% for idx, keyword in keywords_dict.items %}
    <p>{{ idx }}번째 키워드 - {{ keyword.name }}</p>
    <form action="{% url "keyword_delete" keyword.pk%}" method='POST'>
      {% csrf_token %}
      <input type="submit" value='삭제하기'>
    </form>
    <hr>
{% endfor %}
```
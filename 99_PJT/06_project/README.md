# 06주차 Project

### 협업 GIT
- PUSH하려면
내 branch에서 git add . + git commit 해준 뒤,
git switch master로 공용 branch로 간 뒤,
git merge 내 branch 해서 github로 push한다

- PULL하려면
내 branch에서 git add . + git commit 해준 뒤,
git switch master로 공용 branch로 간 뒤,
git pull origin master해서
switch로 다시 돌아온 뒤 merge한다

### 어려운 문장
- base.html에서
<!-- 로그인이 되어 있다면 -->
{% if request.user.is_authenticated %} 

- index.html에서
<!-- 사용자가 좋아요를 누른 리스트에 들어있으면 아래 문장 실행 -->
{% if request.user in movie.like_users.all %} 

- 로그아웃 기능도 form으로 작성
<!-- <form action="{% url "accounts:logout" %}" method='POST'> -->
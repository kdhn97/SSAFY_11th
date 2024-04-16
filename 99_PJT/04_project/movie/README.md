# 버전2. 영화

## accounts 앱
### 로그인 된 경우에만 실행할 것들
- 로그아웃
### 로그인 된 경우 실행하면 안될 것들
- 회원가입
- 회원정보 수정
- 비밀번호 변경
- 회원탈퇴
- 로그인
### 비밀번호 변경 labal과 a태그 없애는 법
`UserChangeForm`에 있는 `password` 속성을 `charfield`로 바꾸고 `widget`을 사용해서 `class`를 `display: none`으로 바꿔줌
`labal`은 `charfield`의 키워드 인자 `labal`값을 `False`로 바꿈

## movies 앱
### 부트스트랩
네이게이션 바와 카드, 버튼 등의 스타일 지정
### context 활용법
#### 상황 1 : html에 movie 인스턴스가 없을 때, movie의 pk를 받아오는 방법 -> context {'movie': movie} 추가
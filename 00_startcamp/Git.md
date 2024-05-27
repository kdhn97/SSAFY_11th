`mkdir 파일명` 파일 만들기

`ls` 해당 폴더 내부 확인

`cd 파일명` 해당 폴더로 이동

`start .` 현재 위치 열기

`touch 파일명` 해당 파일 생성

`git log --oneline` commit 기록 출력

# 순서
### [ push 하는 순서 ]

1. `git add .` 현재 파일 git에 추가
2. `git commit -m “문구”` commit
3. `git push origin master` origin에 master한 것을 git에 push

### [ pull 하는 순서 ]

1. git lab에서 주소 복사
2. 오른쪽 마우스 누르고 Open Git Bash here 클릭
3. `git clone 주소`(shift+insert) 입력

# 자리 옮겼을 때 설정법
- 이전 설정 삭제 : 자격증명관리자 → git 삭제
- 내 설정 등록

`git config —-global [user.email](http://user.email) ‘ ’`

`git config —-global [user.name](http://user.name) ‘ ’`

- 내 설정 확인

`git config —-list`

# Branch
- 장점
    - 독립 공간 형성, **원본이 안전**하다
    - 체계적인 협업과 개발이 가능하다
    - 에러가 발생한 버전을 이전 버전으로 되돌리거나 삭제 가능
- 명령어
    - `git branch` : 브랜치 목록 확인
    - `git branch -r` : 원격 저장소의 브랜치 목록 확인
    - `git branch 브랜치명` : 새로운 브랜치 생성
    - 특정 브랜치 삭제
        - `git branch -d 브랜치명` : 병합된 브랜치만 삭제 가능
        - `git branch -D 브랜치명` : 강제 삭제 (병합 안 된 브랜치도 삭제)
    - 다른 브랜치 이동
        - `git switch 다른 브랜치명` : 다른 브랜치로 이동
        - `git switch -c 브랜치명` : 브랜치를 새로 생성과 동시에 이동
        - `git switch -c 브랜치명 커밋ID` : 특정 커밋을 기준으로 브랜치 생성 + 이동
    - 브랜치 병합
        - `git merge 합칠 브랜치명`
            - branch1를 branch2에 합치려면? `$git switch branch2` `$git merge branch1`
            - 끝내기 `:wq`
    - 병합의 종류
        - Fast-Forward : 빨리감기 (merge 과정없이 단순히 브랜치의 포인트가 이동)
        - 3-Way Merge : **각 브랜치의 커밋 두개와 공통 조상 커밋 하나**를 사용하여 병합
            - 같은 파일의 같은 부분을 수정한 경우 → **충돌** 오류
        - Merge Conflict
- 주의 사항
    - git switch 전 Working Directory 파일이 모두 버전 관리가 되고 있는지 확인해야함

# git Branch 과정
  1. git init → 가상환경 master 시작
2. git add .
3. git commit -m ‘first’
4. git branch practice → practice 브랜치 생성
5. git branch → 브랜치 확인 master, practice 존재함
6. git switch practice → 다른 브랜치로 이동 (master → practice)
7. touch practice.txt → 파일 생성 (작업) 
8. git add .
9. git commit -m ‘ ’
10. 작업물이 practice 가상환경에만 저장됨
11. git switch master → 가상환경 변경 시 작업물 숨겨짐
12. git merge practice → 두 가상환경을 합침
    1. 3-way의 경우 `:wq` 로 작업 끝
13. git branch -d practice → practice 가상환경 삭제

# Undoing
- `git restore 파일명` : 수정 내용을 commit 이전으로 되돌리기
- `git rm --cached 파일명` : 잘못된 git add 파일 삭제하기
- `git restore --staged 파일명` : 잘못된 git commit 파일 삭제하기
- `git commit --amend` : 직전 commit 이름 수정

→ Insert + i 누르고 수정 후 Esc 누르고 빠져나온 뒤 :wq 누르기

- `git reset --mixed (git log --oneline 번호)` 수정한 작업을 남기고 commit 기록만 해당 번호까지 unstaged 상태로 되돌림
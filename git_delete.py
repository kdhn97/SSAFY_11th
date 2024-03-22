# 자동으로 .git 폴더 삭제 해주는 코드
import os # 파이썬 표준 라이브러리 -> 운영 체제와 상호 작용 가능
import subprocess

current_folder = os.getcwd() # 현재 폴더 경로를 변수에 저장
# 현재 폴더 및 모든 하위 폴더를 반복
for foldername, subfolder, filenames in os.walk(current_folder):
    if '.git' in subfolder: # 하위 폴더 목록에 .git이 있다면
        if foldername == current_folder: # root 디렉토리는 제외
            continue
        # 삭제하려는 .git 폴더의 위치를 변수에 저장
        git_folder_path = os.path.join(foldername, '.git')
        # 경로 : 'folder' + '.git' -> folder/.git
        subprocess.run(['rm', '-rf', git_folder_path]) # rm - rf 폴더 경로
        print(f'{git_folder_path} 폴더가 삭제되었습니다.')
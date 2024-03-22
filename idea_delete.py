import os
import shutil

def delete_folder(root_folder, folder_name):
    for folder, subfolders, files in os.walk(root_folder, topdown=False):
        if folder_name in subfolders:
            folder_path = os.path.join(folder, folder_name)
            try:
                shutil.rmtree(folder_path)
                print(f"Deleted folder: {folder_path}")
            except Exception as e:
                print(f"Error deleting folder {folder_path}: {e}")

# 삭제하고자 하는 폴더의 이름과 해당 폴더가 있는 폴더 경로를 지정합니다.
root_folder = "SSAFY_11TH"  # 시작 폴더 경로를 변경하세요.
folder_name = ".idea"  # 삭제하려는 폴더의 이름을 변경하세요.

delete_folder(root_folder, folder_name) # 폴더 삭제 함수 호출

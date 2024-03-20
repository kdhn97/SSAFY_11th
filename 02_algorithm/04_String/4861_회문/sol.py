import sys
sys.stdin = open('input.txt')

# 전치 행렬 생성
def trans():
    for i in range(N):
        for j in range(N):
            if i == j: continue
            if i > j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

# 문자열 완전 탐색 함수
def search(arr):
    def is_palind(word):    # 회문 판별
        return word == word[::-1]

    # 전체 행 or 열 순회
    for i in range(N):
        # 회문의 길이 만큼 뺀 범위 순회
        for j in range(N-M+1):
            check_word = ''
            for k in range(M):
                check_word += arr[i][j+k]   # 범위만큼 문자열 생성
            result = is_palind(check_word)
            if result:
                return check_word
    return False


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]

    result_1 = search(arr)  # 가로 탐색
    trans()                 # 전치행렬 생성 (원본 변경)
    result_2 = search(arr)  # 세로 탐색

    if result_1:
        print(result_1)
    else:
        print(result_2)
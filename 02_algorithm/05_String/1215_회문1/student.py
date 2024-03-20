import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    length = int(input())
    arr = [list(map(str, input())) for _ in range(8)]
    result = 0

    # 행 검사
    for i in range(8):
        for k in range(8 - length + 1):
            cnt = 0
            for j in range(length // 2):
                if arr[i][j+k] == arr[i][length-j-1+k]:
                    cnt += 1
            if cnt >= length//2:        # 회문인지 확인
                result += 1

    # 열 검사
    for j in range(8):
        for k in range(8 - length + 1):
            cnt = 0
            for i in range(length // 2):
                if arr[i+k][j] == arr[length-i-1+k][j]:
                    cnt += 1
            if cnt >= length//2:
                result += 1
    print(f'#{tc} {result}')


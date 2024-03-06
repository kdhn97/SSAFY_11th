import sys
sys.stdin = open('input.txt')

for i in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = 0

    # 행 우선 조회
    for i in range(100):
        tmp = 0
        for j in range(100):
            tmp += arr[i][j]
        if result < tmp:
            result = tmp

    # 열 우선 조회
    for i in range(100):
        tmp = 0
        for j in range(100):
            tmp = arr[j][i]
        if result < tmp:
            result = tmp

    # 좌상 -> 우하
    tmp = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                tmp += arr[i][j]
    if result < tmp:
        result = tmp

    tmp = 0
    for i in range(100):
        tmp += arr[i][i]
    if result < tmp:
        result = tmp

    # 우상 -> 좌하
    # i는 점점 커져야함
    tmp = 0
    for i in range(100):
        # j는 점점 작아져야함
        for j in range(99, -1, -1):
            tmp += arr[i][j]
    if result < tmp:
        result = tmp

    tmp = 0
    for i in range(100):
        tmp += arr[i][99 - i]
    if result < tmp:
        result = tmp


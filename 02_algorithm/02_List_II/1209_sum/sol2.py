import sys
sys.stdin = open('input.txt')

# 과연 짧고 좋을까?

for i in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = 0

    # 좌상 우하
    dia = 0
    # 우상 좌하
    dia_r = 0
    for i in range(100):
        # 행 우선
        row = 0
        # 열 우선
        col = 0
        dia += arr[i][i]
        dia_r += arr[i][99-i]
        for j in range(100):
            row += arr[i][j]
            col += arr[j][i]
        if result < col:
            result = col
        if result < row:
            result = row
    if result < dia:
        result = dia
    if result < dia_r:
        result = dia_r

    print(f'#{tc} {result}')

import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = 1
    # 3x3 범위 조사시 중복되는수가 1개 이상일시
    # tmp의 길이가 9가 아니게 됨
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            tmp = set()
            for x in range(i, i+3):
                for y in range(j, j+3):
                    tmp.add(arr[x][y])
            if len(tmp) != 9:
                result = 0
                break
        if not result:
            break

    for x in range(9):
        tmp = set()
        tmp_2 = set()
        for y in range(9):
            tmp.add(arr[x][y])
            tmp_2.add(arr[y][x])
        if len(tmp) != 9 or len(tmp_2) != 9:
            result = 0
            break
    print(f'#{tc} {result}')
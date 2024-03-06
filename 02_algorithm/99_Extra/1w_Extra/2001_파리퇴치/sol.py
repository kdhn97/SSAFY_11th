import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            tmp = 0
            for x in range(i, i+M):
                for y in range(j, j+M):
                    tmp += arr[x][y]
            if result < tmp:
                result = tmp
    print(f'#{tc} {result}')
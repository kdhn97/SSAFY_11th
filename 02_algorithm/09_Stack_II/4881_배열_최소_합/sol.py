import sys
sys.stdin = open('input.txt')


def saerch(r, cnt):
    global result
    if cnt > result:
        return
    if r == N:
        if result > cnt:
            result = cnt
            return
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                saerch(r+1, cnt + arr[r][i])
                visited[i] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 11*N
    visited = [0] * N
    saerch(0, 0)
    print(f'#{tc} {result}')
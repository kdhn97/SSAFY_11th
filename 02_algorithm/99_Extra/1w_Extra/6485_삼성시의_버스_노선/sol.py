import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    Cj = [int(input()) for _ in range(P)]
    station = [0] * 5001
    for i in range(N):
        for x in range(arr[i][0], arr[i][1] + 1):
            station[x] += 1

    result = [station[s] for s in Cj]
    print(f'#{tc}', *result)
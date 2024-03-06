import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(Q)]

    result = [0] * (N + 1)
    for i in range(Q):
        for j in range(arr[i][0], arr[i][1]+1):
            result[j] = i + 1
    print(f'#{tc}', *result[1:])


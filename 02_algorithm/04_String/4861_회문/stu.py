import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]
    K = 0   # k 값 받아줄 변수
    result = []
    # 행 탐색
    for i in range(N):
        cnt = 0
        for j in range(M//2):
            for k in range(N-M+1):
                if arr[i][j+k] == arr[i][M-j+k-1]:
                    cnt += 1
                    K = k
            if cnt >= M//2:
                result.extend(arr[i][K:K+M+1])
                print(f'#{tc}', end=' ')
                print(*result, sep='')
                break

    # 열 탐색
    # 전치행렬
    rev_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(M):
            rev_arr[i][j] = arr[j][i]

    for i in range(N):
        cnt = 0
        for j in range(M//2):
            for k in range(N-M+1):
                if rev_arr[i][j+k] == rev_arr[i][M-j+k-1]:
                    cnt += 1
                    K = k
            if cnt >= M//2:
                result.extend(rev_arr[i][K:K+M+1])
                print(f'#{tc}', end=' ')
                print(*result, sep='')
                break


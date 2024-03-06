T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    max_pang = 0 # 최대 꽃가루 합계

    for i in range(N): # N X M 크기의 게임판
        for j in range(M):
            pang = arr[i][j] # 터트린 풍선의 꽃가루 횟수

            for k in range(4): # arr[i][j] 횟수만큼 퍼지기
                for l in range(1, arr[i][j] + 1):
                    ni = i + di[k] * l
                    mj = j + dj[k] * l
                    # 격자 범위 내에서만
                    if 0 <= ni < N and 0 <= mj < M:
                        pang += arr[ni][mj]
            # 최대 풍선팡 구하기
            if max_pang < pang:
                max_pang = pang

    print(f'#{test_case} {max_pang}') # #1 10
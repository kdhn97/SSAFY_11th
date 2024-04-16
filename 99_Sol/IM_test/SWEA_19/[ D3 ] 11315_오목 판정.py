def A(arr):
    # 가로,세로,대각선,역대각선
    dr = [0,1,1,1]
    dc = [1,0,1,-1]
    for start_r in range(N):
        for start_c in range(N):
            if arr[start_r][start_c] == 'o':
                for d in range(4):
                    r = start_r
                    c = start_c
                    # 각 방향으로 연속적으로 오목이 존재하는가?
                    cnt = 0
                    while 0 <= r <= N-1 and 0 <= c <= N-1 and arr[r][c] == 'o':
                        cnt += 1
                        r += dr[d]
                        c += dc[d]
                    if cnt >= 5:
                        return 'YES'
    return 'NO'

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    print(f'#{tc} {A(arr)}')
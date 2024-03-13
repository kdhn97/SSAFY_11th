T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = []
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            else:
                result.append(cnt)
                cnt = 0
        result.append(cnt)

    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
            else:
                result.append(cnt)
                cnt = 0
        result.append(cnt)

    cnt_re = 0
    for k in range(len(result)):
        if result[k] == M:
            cnt_re += 1
    print(f'#{test_case} {cnt_re}')
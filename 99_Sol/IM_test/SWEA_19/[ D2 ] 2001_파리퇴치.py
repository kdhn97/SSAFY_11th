T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    fly = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            lst_fly = []
            for a in range(M):
                for b in range(M):
                    if 0 <= i < N and 0 <= j < N:
                        lst_fly.append(fly[i+a][j+b])
            sum_fly = sum(lst_fly)
            if result < sum_fly:
                result = sum_fly
    print(f'#{test_case} {result}') # #1 49
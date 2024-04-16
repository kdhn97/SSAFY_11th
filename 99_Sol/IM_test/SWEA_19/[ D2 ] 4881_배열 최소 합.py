T = int(input()) # T: 3
for test_case in range(1, T+1): # test_case: 1
    def f(i, k, cnt): # cnt: 선택한 원소의 합
        global min_v
        if i == k:
            if min_v > cnt:
                min_v = cnt
        elif cnt >= min_v: # 원소의 합이 min_v보다 크면
            return # 거른다
        else:
            for j in range(i, k):  # P[i]자리에 올 원소 P[j]
                P[i], P[j] = P[j], P[i]  # P[i] <-> P[j]
                f(i+1, k, cnt+arr[i][P[i]])
                P[i], P[j] = P[j], P[i]  # 교환 전으로 복구

    N = int(input()) # N: 3
    arr = [list(map(int, input().split())) for _ in range(N)] # arr: [[2,1,2],[5,8,5],[7,2,2]]
    P = [ _ for _ in range(N) ] # P: [0,1,2]
    min_v = 100
    f(0, N, 0)
    print(f'#{test_case} {min_v}') # #1 8
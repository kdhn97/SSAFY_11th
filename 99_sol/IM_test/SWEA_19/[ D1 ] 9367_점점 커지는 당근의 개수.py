T = int(input())
for test_case in range(1, T+1): # test_case: 1
    N = int(input()) # N: 5
    C = list(map(int, input().split())) # C: 1 2 3 4 5
    # 연속으로 커지지않는 경우 구간의 최소 길이는 1
    arr = [1] * N # [1, 1, 1, 1, 1]
    for i in range(1, N):
        if C[i] - C[i-1] > 0:
            arr[i] = arr[i-1] + 1
    # 연속으로 커지는 당근 개수의 최대값을 출력한다.
    print(f'#{test_case} {max(arr)}') # #1 5
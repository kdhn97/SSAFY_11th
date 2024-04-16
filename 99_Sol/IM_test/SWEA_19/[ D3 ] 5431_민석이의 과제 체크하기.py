T = int(input()) # 11
for test_case in range(1, T+1):
    N, K = list(map(int, input().split())) # 5 3
    student = list(map(int, input().split()))  # 2 5 3

    result = list(range(1, N+1))

    for n in range(1, N+1):
        if n in student:
            result.remove(n)
    print(f'#{test_case} {" ".join(map(str, result))}') # #1 1 4
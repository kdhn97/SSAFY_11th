T = int(input())
for test_case in range(1, T + 1):
    result = [0] * 5001
    answer = []

    N = int(input())
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            result[i] += 1

    P = int(input())
    for j in range(P):
        p = int(input())
        answer.append(result[p])

    print(f'#{test_case}', *answer)
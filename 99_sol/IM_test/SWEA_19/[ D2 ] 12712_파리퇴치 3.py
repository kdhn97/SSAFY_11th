T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    ti = [1, 0, -1, 0]
    tj = [0, 1, 0, -1]
    xi = [1, -1, 1, -1]
    xj = [1, 1, -1, -1]

    result = []
    for i in range(N):
        for j in range(N):
            answer = 0
            for k in range(1, M):
                for a in range(4):
                    x = i + ti[a] * k
                    y = j + tj[a] * k
                    if 0 <= x < N and 0 <= y < N:
                        answer += arr[x][y]
            result.append(answer+arr[i][j])

    for i in range(N):
        for j in range(N):
            answer = 0
            for k in range(1, M):
                for a in range(4):
                    x = i + xi[a] * k
                    y = j + xj[a] * k
                    if 0 <= x < N and 0 <= y < N:
                        answer += arr[x][y]
            result.append(answer+arr[i][j])

    print(f'#{test_case} {max(result)}')
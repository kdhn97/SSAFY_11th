T = int(input()) # 1
for test_case in range(1, T+1):
    N, K = list(map(int, input().split())) # 3 1
    score = list(map(int, input().split())) # 100 90 80

    result = 0
    for k in range(K):
        result += max(score)
        score.remove(max(score))
    print(f'#{test_case} {result}') # #1 100
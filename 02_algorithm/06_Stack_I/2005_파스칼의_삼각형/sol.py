import sys
sys.stdin = open('input.txt')

memo = [[1] * 10 for _ in range(10)]

for i in range(1, 10):
    for j in range(1, 10):
        if i != j:
            memo[i][j] = memo[i-1][j-1] + memo[i-1][j]

T = int(input())
for test_case in range(1, T+1): # test_case: 1
    N = int(input())
    for i in range(N):
        print(*memo[i][:i+1])


    # N = int(input()) # N: 4
    # pascal = [[0] * N for _ in range(N)] # 계산 후 정리할 공간
    # pascal[0][0] = 1
    # for i in range(1, N):
    #     for j in range(N):
    #         # print(i, j)
    #         if j == 0:
    #             pascal[i][j] = 1
    #         else:
    #             pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    # print(f'#{test_case}')
    # for k in range(N):
    #     for l in range(N):
    #         # print(k, l)
    # #         if pascal[k][l]:
    # #             print(pascal[k][l], end=' ')
    # #     print()
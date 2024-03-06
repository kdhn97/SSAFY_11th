import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(str, input().split())) for _ in range(N)]

    # 90도
    degree_90 = []
    for i in range(N): # 0 1 2
        tmp = ''
        for j in range(N-1, -1, -1): # 2 1 0
            tmp += data[j][i]
        degree_90.append(tmp)

    # 180도
    degree_180 = []
    for i in range(N-1, -1, -1): # 2 1 0
        tmp = ''
        for j in range(N-1, -1, -1): # 2 1 0
            tmp += data[i][j]
        degree_180.append(tmp)

    # 270도
    degree_270 = []
    for i in range(N-1, -1, -1): # 2 1 0
        tmp = ''
        for j in range(N): # 0 1 2
            tmp += data[j][i]
        degree_270.append(tmp)
    print(f'#{tc}')
    for i in range(N):
        print(degree_90[i], degree_180[i], degree_270[i])
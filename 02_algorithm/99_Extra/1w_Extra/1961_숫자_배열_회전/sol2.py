import sys
sys.stdin = open('input.txt')

def turn(arr):
    result = []
    for i in range(N): # 0 1 2
        tmp = ''
        for j in range(N-1, -1, -1): # 2 1 0
            tmp += arr[j][i]
        result.append(tmp)
    return result


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(str, input().split())) for _ in range(N)]

    # 90도
    degree_90 = turn(data)

    # 180도
    degree_180 = turn(degree_90)

    # 270도
    degree_270 = turn(degree_180)

    print(f'#{tc}')
    for i in range(N):
        print(degree_90[i], degree_180[i], degree_270[i])
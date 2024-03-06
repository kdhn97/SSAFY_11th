import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    result = 0
    tmp = 0
    for i in range(0, N):
        if arr[i] == 1:
            tmp += 1
        else:
            tmp = 0
        if tmp >= result:
            result = tmp
    print(f'#{tc} {result}')



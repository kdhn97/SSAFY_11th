import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    while M:
        arr.append(arr.pop(0))
        M -= 1
    print(f'#{tc} {arr[0]}')

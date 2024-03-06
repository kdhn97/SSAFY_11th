import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(range(1, 13))

    for i in range(1 << 12):
        result = []
        for j in range(12):
            if i & (1 << j):
                result.append(arr[j])
        if len(result) == N and sum(result) == K:
            print(f'#{tc} 1')
            break
    else:
        print(f'#{tc} 0')

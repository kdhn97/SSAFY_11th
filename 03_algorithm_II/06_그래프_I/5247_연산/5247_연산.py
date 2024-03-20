import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split()) # 2, 7

    cnt = 0
    while N != M: # N과 M이 같지 않다면
        if N+1 == M or N-1 == M or N*2 == M or N-10 == M:
            cnt += 1
            break
        else:
            if M > N*2 and M % 2 == 0:
                cnt += 1
                M //= 2

            if M % 2 == 1:
                cnt += 1
                M -= 1

            if M < N and N-M > 5:
                cnt += 1
                M += 10
            elif M < N and N-M <= 5:
                cnt += 1
                M += 1

    print(f'#{test_case} {cnt}')
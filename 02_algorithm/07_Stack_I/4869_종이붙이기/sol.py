import sys
sys.stdin = open('input.txt')

memo = [0, 1, 3]
for i in range(2, 30):
    memo.append(memo[i] + memo[i-1]*2)
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {memo[N//10]}')
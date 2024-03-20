import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())

for tc in range(1, T+1):
    password = deque(map(int, input().split()))
    # print(password)
    cycle = 1   # 처음엔 1을 뺌
    while password[-1] != 0:    # 마지막 수가 0이 아닌동안 순회
        now = password.popleft(0) - cycle
        # now -= cycle
        cycle += 1  # 2번째는 2, 3번째는 3, 4번째는 4...
        if now <= 0:    # 뺴다가 음수가 되면
            now = 0     # 음수는 안됨. 0으로 바꿔버림
        if cycle == 6:  # 암호에서 뺴나갈 수는 1~5까지임. 6이되면 다시 1부터시작
            cycle = 1
        password.append(now)
    print(f'#{tc}', *password)
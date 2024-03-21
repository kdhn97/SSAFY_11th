import sys
sys.stdin = open("input.txt", "r")
# 너비 우선 탐색(BFS)을 사용하여 한 숫자에서 다른 숫자로 이동하는 최소 횟수를 찾는 문제
from collections import deque

T = int(input())
for test_case in range(1, T+1): # test_case: 1
    N, M = map(int, input().split()) # N: 2, M: 7
    visit = [0] * 1000001 # 방문 여부를 나타내는 리스트 생성 / 연산 결과 * 100만까지
    queue = deque([N]) # 큐 생성 # queue: deque([2]) -> deque([3, 1, 4])

    while visit[M] == 0: # 목표 숫자의 횟수가 0 == 아직 도착 못함
        now = queue.popleft() # 큐에서 현재 숫자를 가져옴
        # 현재 숫자에서 가능한 연산을 수행하여 새로운 숫자 생성
        for i in [now+1, now-1, now*2, now-10]: # [3, 1, 4, -8]
            # 숫자가 연산 범위 100만 이내에 있고 방문하지 않았다면
            if 0 < i <= 1000000 and visit[i] == 0:
                visit[i] = visit[now] + 1 # 연산 횟수 표시
                queue.append(i) # 새로운 숫자를 큐에 추가하여 다음 탐색 대상으로 설정

    print(f'#{test_case} {visit[M]}')
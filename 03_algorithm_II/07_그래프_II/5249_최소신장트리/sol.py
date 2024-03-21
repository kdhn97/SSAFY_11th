import sys
sys.stdin = open('input.txt')

from heapq import heappush, heappop

def prim(start):
    pq = [] # 우선순위 큐
    visited = [0] * (V + 1) # 방문 표시 # visited: [0, 0, 0]
    sum_weight = 0 # 최소 비용
    # [PRIM] 가중치가 낮으면 먼저 나와야 함 : 가중치, 노드 번호 관리
    heappush(pq, (0, start)) # 시작점 추가

    while pq:
        # 0 -> weight, start -> now로 가게 됨
        weight, now = heappop(pq)
        if visited[now]: # 방문했다면 Pass
            continue
        visited[now] = 1 # 방문 처리
        sum_weight += weight # 누적합 추가
        for to in range(1, V + 1): # 갈 수 있는 노드들을 보면서
            # 갈 수 없거나 이미 방문했다면 Pass
            if graph[now][to] == 0 or visited[to]:
                continue
            # 갈 수 있으면서 방문하지 않았다면
            heappush(pq, (graph[now][to], to))
    print(f'#{test_case} {sum_weight}') #1 2

T = int(input())
for test_case in range(1, T+1): # test_case: 1
    V, E = map(int, input().split()) # V: 2, E: 3
    # 인접 행렬로 저장 # graph: [[0, 1, 1], [1, 0, 6], [1, 6, 0]]
    graph = [[0] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        # [가중치 그래프] s -> e로 가는데 w이라는 비용이 든다
        graph[s][e] = w
        graph[e][s] = w # 무방향 그래프
    prim(0)

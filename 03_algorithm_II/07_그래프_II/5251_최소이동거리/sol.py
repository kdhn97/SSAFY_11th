import sys
sys.stdin = open('input.txt')
# 다익스트라 알고리즘 함수 정의
from heapq import heappush, heappop

def dijkstra(start):
    pq = [] # 우선순위 큐
    heappush(pq, (0, start)) # 시작점의 weight, node 번호를 한 번에 저장
    distance[start] = 0 # 시작 노드의 거리 초기화

    while pq:
        dist, now = heappop(pq) # 우선순위 큐에서 가장 거리가 짧은 노드 pop
        # now가 이미 더 짧은 거리로 온 적 있다면 Pass
        if distance[now] < dist:
            continue
        for to in graph[now]: # now에서 인접한 다른 노드 확인
            next_dist = to[0] # 다음 노드까지의 거리
            next_node = to[1] # 다음 노드 번호
            new_dist = dist + next_dist # 누적 거리 계산
            # 이미 더 짧은 거리로 간 경우 Pass
            if new_dist >= distance[next_node]:
                continue
            distance[next_node] = new_dist # 누적 거리를 최단 거리로 갱신
            # next_node의 인접 노드들을 우선순위 큐에 추가
            heappush(pq, (new_dist, next_node))

T = int(input())
for test_case in range(1, T+1):
    INF = int(1e9)  # 1e9 : 10억 -> 무한대 값 설정
    V, E = map(int, input().split()) # V: 2, E: 3
    start = 0 # 시작 노드 번호 # start: 0
    # 인접 리스트
    graph = [[] for _ in range(V+1)] # graph: [[[1, 1], [6, 2]],[[1, 2], []]
    distance = [INF] * (V+1) # 누적 거리를 저장할 리스트
    # 간선 정보 저장
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append([w, e])

    dijkstra(0)
    # print(distance) # [0, 1, 2]
    print(f'#{test_case} {distance[-1]}') #1 2
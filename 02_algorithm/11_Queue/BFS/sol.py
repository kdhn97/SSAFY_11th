import sys
sys.stdin = open('input.txt')

from collections import deque

def BFS(S):
    visited[S] = 1
    q = deque()
    q.append(S)
    while q:
        print(q)
        now = q.popleft()
        print(now, end=' ')
        for next in adj[now]:
            if not visited[next]:
                visited[next] = 1
                q.append(next)

V, E = map(int, input().split())
edge = list(map(int, input().split()))

visited = [0] * (V+1)   # 0번 노드 없음
adj = [[] for _ in range(V+1)]  # 0번 노드 없음
for i in range(0, E*2, 2):  # 모든 간선 정보에 대해
    adj[edge[i]].append(edge[i+1])  # 무방향 그래프이므로 양 방향으로
    adj[edge[i+1]].append(edge[i])
print(adj)
BFS(1)

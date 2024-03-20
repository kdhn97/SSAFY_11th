import sys
sys.stdin = open('input.txt')

from collections import deque

def BFS(S, G):
    q = deque()
    q.append((S, 0))    # 시작 지점과 이동 횟수 기록
    while q:
        now, cnt = q.popleft()
        visited[now] = 1    # 방문 표시
        # print(now, cnt)
        # print(visited)
        for w in adj[now]:  # 현재 위치 기준 이동 가능 노드 탐색
            if not visited[w]:  # 해당 지점 방문 기록 없다면
                if w == G:      # 해당 지점 도착지라면
                    return cnt + 1  # 이동 횟수 + 1 반환하며 코드 종료
                q.append([w, cnt+1])    # 이동 및 이동 횟수 1 증가


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    visited = [0] * (V+1)               # 0번 노드 없음 -> V번 인덱스 필요
    adj = [[] for _ in range(V+1)]      # 0번 노드 없음 -> V번 인덱스 필요
    for e in edge:
        adj[e[0]].append(e[1])          # 양방향 그래프이므로 양쪽다 표기
        adj[e[1]].append(e[0])
    result = BFS(S, G)
    print(f'#{tc} {result}')

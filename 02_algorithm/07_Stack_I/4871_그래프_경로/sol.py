import sys
sys.stdin = open('input.txt')

def DFS(start):
    visited[start] = 1          # 방문 표시
    for next in adj[start]:     # 인접 노드 순회
        if not visited[next]:   # 방문한적 없으면
            DFS(next)           # 이동

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())    # 정점 수, 간선 수
    # 간선 정보
    edge = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())    # 시작, 끝
    visited = [0] * (V + 1)             # 방문 정보
    adj = [[] for _ in range(V+1)]      # 인접 리스트 (0번 노드 없음)
    for i in range(E):                  # 간선 정보 표기
        adj[edge[i][0]].append(edge[i][1])  # 단방향이므로 한쪽만 표기
    DFS(S)                              # 탐색 시작
    result = visited[G]                 # G 지점에 도착한 적 있는지 판별
    print(f'#{tc} {result}')
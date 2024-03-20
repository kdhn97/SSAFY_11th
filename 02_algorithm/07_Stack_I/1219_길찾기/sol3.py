import sys
sys.stdin = open('input.txt')

def DFS(start):
    visited[start] = 1  # 현재 위치 방문 표기
    stack = [start]

    while stack:
        now = stack.pop()
        visited[now] = 1
        for next in adj[now]:
            if not visited[next]:
                stack.append(next)

for _ in range(10):
    tc, N = map(int, input().split())
    edge = list(map(int, input().split()))

    visited = [0] * 100
    adj = [[] for _ in range(100)]  # 0부터 99까지
    for i in range(N):
        adj[edge[i*2]].append(edge[i*2+1])

    DFS(0)  # 시작지점 0으로 고정
    print(f'#{tc} {visited[99]}')   # 도착지점 99로 고정
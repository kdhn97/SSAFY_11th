import sys
sys.stdin = open('input.txt')

def DFS(start):
    visited[start] = 1  # 현재 위치 방문 표기
    for next in range(100):
        if adj[start][next] and not visited[next]:
            DFS(next)

for _ in range(10):
    tc, N = map(int, input().split())
    edge = list(map(int, input().split()))
    visited = [0] * 100

    adj = [[0] * 100 for _ in range(100)]  # 인접 행렬
    for i in range(N):
        adj[edge[i*2]][edge[i*2+1]] = 1


    DFS(0)  # 시작지점 0으로 고정
    print(f'#{tc} {visited[99]}')   # 도착지점 99로 고정
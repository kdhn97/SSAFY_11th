import sys
sys.stdin = open('input.txt')

def DFS(start):
    visited[start] = 1  # 현재 위치 방문 표기

    # 길이 있고, 방문한 적 없다면
    if adj_1[start] >= 0 and not visited[adj_1[start]]:
        DFS(adj_1[start])   # 해당 위치로 방문
    # 다른 길
    if adj_2[start] >= 0 and not visited[adj_2[start]]:
        DFS(adj_2[start])   # 해당 위치로 방문

for _ in range(10):
    tc, N = map(int, input().split())
    edge = list(map(int, input().split()))
    adj_1 = [-1] * 100  # 0번 노드 사용 예정
    adj_2 = [-1] * 100
    visited = [0] * 100
    # print(edge)
    for i, idx in enumerate(range(0, N*2, 2)):
        if i % 2:
            adj_2[edge[idx]] = edge[idx+1]
        else:
            adj_1[edge[idx]] = edge[idx+1]

    DFS(0)  # 시작지점 0으로 고정
    print(f'#{tc} {visited[99]}')   # 도착지점 99로 고정
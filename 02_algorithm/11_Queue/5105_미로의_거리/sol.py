import sys
sys.stdin = \
    open('input.txt')

from collections import deque

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    visited = [[0] * N for _ in range(N)]   # 방문 표시
    q = deque([(x, y, 0)])  # 시작 좌표, 이동 거리 기록
    while q:    # 모든 탐색 대상 조사할때 까지
        x, y, cnt = q.popleft()
        for k in range(4):  # 4방향 탐색
            nx = x + dx[k]
            ny = y + dy[k]
            # 범위내이며, 방문한적 없다면
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if maze[nx][ny] == 0:   # 통로인 경우
                    visited[nx][ny] = 1 # 방문 표시 후
                    q.append((nx, ny, cnt + 1)) # 이동 거리 1증가하고 이동
                elif maze[nx][ny] == 3: # 도착지인 경우
                    return cnt          # 도착
    # 모든 경로를 다 조사했지만 도착하지 못했다면
    # 조사도중 return (함수가 종료) 될 수 있는 경우는
    # 도착지 (값이 3인 위치)에 도달한 경우 밖에 없으므로
    # while문이 종료될 때까지 (q가 빌때까지, 모든 조사를 완료할 때 까지)
    # return 되지 않았다면 도착할 수 없음을 의미
    return 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    result = None
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:     # 출발지 탐색
                result = BFS(i, j)  # 출발
                # 출발지에서 이동 가능한 모든 경로를 탐색했으므로
                # 다른 좌표에 대한 탐색 진행할 필요 없음
                break
        if result != None:  # result의 값이 바꼈다면
            # 출발지로부터 조사를 진행한 이후이므로
            # 다른 좌표에 대한 탐색 진행할 필요 없음
            break
    print(f'#{tc} {result}')
import sys
sys.stdin = open('input.txt')

def dfs(now, destIdx):
    global cnt
    if now == dest[destIdx]:
        if destIdx == M - 1:
            cnt += 1
            return
        else:
            destIdx += 1
    x, y = now # 현재 위치
    visit[x][y] = True # 방문 표시
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i] # 델타 탐색
        if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == False and arr[x][y] == 0:
            dfs([nx, ny], destIdx)
    visit[x][y] = False # 초기화
    return

N, M = map(int, input().split()) # N: 3, M: 3
arr = [list(map(int, input().split())) for _ in range(N)] # [[0,0,0],[0,0,0],[0,0,1]]
dest = [] # 목적지 [[2,0],[0,1],[1,2]]
for _ in range(N):
    x, y = map(int, input().split())
    dest.append([x-1, y-1])
visit = [[False for _ in range(N)] for _ in range(N)] # 방문 표시
cnt = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dfs(dest[0], 1)
print(cnt)
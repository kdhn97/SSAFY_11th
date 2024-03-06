import sys
sys.stdin = open('input.txt')

# 낱말은 오른쪽 혹은 아래로만 입력가능
    # 하, 우
dx = [1, 0]
dy = [0, 1]

def check(x, y, move):
    if move == 0:   # 세로 쓰기
        # 시작지점이 가장 윗 줄이고, 다음줄이 빈칸이면
        if x == 0 and puzzle[x+1][y] == 1: return True
        # 첫 줄이 아닐떄는, 위가 막혀있고, 아래가 뚫려있을 떄만
        if 1 <= x < N-1 and puzzle[x+1][y] == 1 and puzzle[x-1][y] == 0 : return True
    else:           # 가로 쓰기
        # 시작지점이 가장 왼쪽 줄이고, 다음 칸이 빈칸이면
        if y == 0 and puzzle[x][y+1] == 1: return True
        # 가장 왼쪽이 아닐때는, 왼쪽이 막혀있고, 오른쪽이 뚫려있을 때만
        if 1 <= y < N-1 and puzzle[x][y+1] == 1 and puzzle[x][y-1] == 0 : return True
    return False

def search(x, y):
    result = 0

    for i in range(2):
        if check(x, y, i):  # 조사시작 가능한지 체크
            nx = x      # 한 위치에서 양 방향으로 조사 할 수 있으므로
            ny = y      # 원본을 그대로 둔 채 조사
            cnt = 1     # 첫 시작 글자 1개
            while True:
                nx = nx + dx[i] # 다음 위치 조사
                ny = ny + dy[i]
                # 다음 위치가 범위를 벗어나지 않고 빈칸이면
                if 0 <= nx < N and 0 <= ny < N and puzzle[nx][ny] == 1:
                    cnt += 1    # 한 칸 더 작성 가능
                else:
                    break       # 아니면 종료

            if cnt == K:        # 모든 조사를 완료했을때 K만큼만 입력가능하면
                result += 1     # 입력 가능 경우 1증가
    return result



T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(N):
            if puzzle[i][j] == 1:
                result += search(i, j)
    print(f'#{tc} {result}')
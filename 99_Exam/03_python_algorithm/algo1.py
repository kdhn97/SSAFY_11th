import sys
sys.stdin = open('algo1_sample_in.txt')

# 상, 상상, 하, 하하, 좌, 좌좌, 우, 우우
dx = [-1, -2, 1, 2, 0, 0, 0, 0]
dy = [0, 0, 0, 0, -1, -2, 1, 2]

def search(x, y):
    global result
    count = data[x][y]  # 조사 시작지점 점수부터
    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]
        # 범위 벗어나지 않는다면,
        if 0 <= nx < N and 0 <= ny < N:
            count += data[nx][ny]   # 새 위치의 값을 더한 뒤
    if result < count:  # 최댓값 갱신
        result = count

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    # 전수 조사
    for x in range(N):
        for y in range(N):
            search(x, y)
    print(f'#{tc} {result}')
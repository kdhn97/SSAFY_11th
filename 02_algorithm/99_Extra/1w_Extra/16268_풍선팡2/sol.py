import sys
sys.stdin = open('input.txt')

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def delta_search():
    global result
    # 모든 방향 탐색 | 가로 M, 세로 N 주의
    for x in range(N):
        for y in range(M):
            cnt = matrix[x][y]      # 첫 풍선 위치 개수로 초기화
            for i in range(4):      # 4방향 탐색
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M:     # matrix 범위 내라면
                    cnt += matrix[nx][ny]           # 해당 위치 값 추가
            if result < cnt:    # 최댓값 초기화
                result = cnt

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    delta_search()
    print(f'#{tc} {result}')
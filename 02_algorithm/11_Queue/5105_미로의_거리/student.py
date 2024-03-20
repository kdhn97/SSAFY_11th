import sys
sys.stdin = open('input.txt')


q = []
def bfs(si, sj, ei, ej) :
    # 스택에 출발지의 x,y좌표를 리스트로 넣는다
    q.append([si, sj])
    # 출발지를 지나갔으므로 visited에 1을 넣음
    visited[si][sj] = 1

    # 상하좌우 확인
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]

    # q에 있는 동안 반복
    while q :
        # t는 현재 위치의 좌표
        t = q.pop(0)

        # 반복하면서 현재점의 상하좌우에 위치한 점을 확인
        for i in range(4) :
            temp_i = t[0] + di[i]
            temp_j = t[1] + dj[i]

            # 만약 그 점이 범위 안에 있고
            if 0 <= temp_i < N and 0 <= temp_j < N :
                # 벽이 아니고 기존에 방문한 적 없었다면
                if arr[temp_i][temp_j] != 1 and visited[temp_i][temp_j] == 0 :
                    # 그쪽으로 가야하니까 visited를 1로 한다
                    visited[temp_i][temp_j] = 1
                    # 확인하고 있는 점은 기존의 점에서 한 칸 더 간 거니까 +1
                    adjl[temp_i][temp_j] = adjl[t[0]][t[1]] + 1
                    # 확인하고 있는 점을 함수에 넣으며 반복
                    bfs(temp_i, temp_j, ei, ej)

    # 도착점의 최소 거리를 반환한다
    return adjl[ei][ej]


T = int(input())

# 테스트 케이스 입력받음
for tc in range(1, T+1) :
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    # 방문 했는지 아닌지 알 리스트
    visited = [[0 for _ in range(N)] for _ in range(N)]
    # 거리를 더할 리스트
    adjl = [[0 for _ in range(N)] for _ in range(N)]

    # 출발지와 도착지 좌표를 구함
    for i in range(N) :
        for j in range(N) :
            if arr[i][j] == 2 :
                start_i = i
                start_j = j
            if arr[i][j] == 3 :
                end_i = i
                end_j = j

    # 함수에 출발지의 x, y좌표와 도착지의 x, y좌표 입력
    result = bfs(start_i, start_j, end_i, end_j)

    # 마약 도착점의 최소 거리가 0이상이라면 도착한 것이다
    if result > 0 :
        # 이동하는 칸은 출발점부터 도착점까지에 있는 칸이니까 -1
        print(f'#{tc}', result - 1)
    # 0보다 작으면 도착하지 못한 거니까 0 출력
    else :
        print(f'#{tc}', 0)
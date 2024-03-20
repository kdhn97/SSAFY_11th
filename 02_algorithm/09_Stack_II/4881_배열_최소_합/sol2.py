import sys
sys.stdin = open('input.txt')


def process_solution(cnt):  # 최종 문제 해결을 위한 함수
    global result
    if cnt < result:        # 누적값이 답안보다 작다면
        result = cnt        # 교체

def make_candidates(visited, col, N, c):
    in_perm = [False] * NMAX
    for i in range(1, col):
        in_perm[visited[i]] = True

    ncands = 0
    for i in range(1, N+1):
        if in_perm[i] == False:
            c[ncands] = i
            ncands += 1
    return ncands

def backtrack(visited, col, N, cnt):
    global MAXCANDIDATES, result
    if cnt > result:    # 누적값이 최종값보다 크면 유망성 없음
        return
    c = [0]*MAXCANDIDATES   # 사용여부 작성용 배열

    if col == N:        # 열이 N에 도달했다면 모두 조사완료
        process_solution(cnt)   # 누적값으로 답안 여부 판단
    else:
        col += 1
        # 사용 여부, 지금까지 조사한 열, 조사해야 하는 수, 후보군
        ncands = make_candidates(visited, col, N, c)    # 만들어낸 후보군 수만큼 집어넣기
        for i in range(ncands):
            # 해당 열(col)에서 사용할 행(row) idx 기록
            visited[col] = c[i] # c[i] 번째에는 몇번째 행의 값을 쓸 것인지를 기록
            # 값을 추가, 이때, 열이 작업시작 전에 1증가하였으므로 이전 열의 값으로 기록
            backtrack(visited, col, N, cnt + arr[col-1][visited[col]-1])
            # 썼던 것 제자리로
            visited[col] = 0

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    MAXCANDIDATES = N+1     # 최대 후보군 개수
    NMAX = N+1              # 최대 N의 크기
    data = [i for i in range(N+1)]
    visited = [0] * NMAX    # 모든 N에 대한 사용여부
    result = N**2*10     # 충분히 큰수

    backtrack(visited, 0, N, 0)   # 사용여부, 행 조사, 전체 크기, 누적값
    print(f'#{tc+1} {result}')
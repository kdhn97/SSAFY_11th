import sys
sys.stdin = open('algo1_sample_in.txt')

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 조사 범위에 해당하는 모든 칸 (x, y)에 대해서 상하 좌우 조사
def search(x, y):
    global result
    # x, y 번째의 값은 뺀다.
    tmp = -arr[x][y]# 조사한 위치의 모든 값들을 더하기 위한 변수
    for i in range(4):  # 4방향에 대한 조사
        nx = x + dx[i]  # 조사 시작한 x에 대해서 i번째 방향에 대한
        ny = y + dy[i]  # 다음 위치 (상하좌우 중 하나) 의 좌푯값 설정
        # 조사 대상 범위를 애초부터 범위를 벗어나는 경우가 없도록 설정
        tmp += arr[nx][ny]  # 델타탐색인데 왜 if문 없이 그냥 더함?
    # 보너스 점수가 짝수면 2배
    if tmp % 2 == 0:
        tmp = tmp * 2
    # 모든 방향 조사 완료후, 글로벌에 있는 최종 결괏값보다 큰지 작은지 판별
    if result < tmp:
        result = tmp

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0  # 최종 결괏값
    '''
        보너스 점수에 해당하는 부분이 범위를 벗어나면
        0점 처리 될 것이다.
    '''
    for i in range(1, N-1):  # 문제 조건상 불필요한 부분
        for j in range(1, N-1):  # 제외 하고 조사 진행
            search(i, j)    # 전수 조사 진행
    print(f'#{tc} {result}')

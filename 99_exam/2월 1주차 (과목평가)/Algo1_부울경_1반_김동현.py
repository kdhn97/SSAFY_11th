import sys
sys.stdin = open('algo1_sample_in.txt')
### 강사님 코드 ###
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 조사범위에 해당하는 모든 칸 (x, y)에 대해서 상하좌우 조사
def search(x, y):
    global result
    # x, y번째의 값은 뺀다
    tmp = -arr[x][y] # 조사한 위치의 모든 값들을 더하기 위한 변수
    for i in range(4): # 4방향에 대한 조사
        nx = x + dx[i] # 조사 시작한 x에 대해서 i번째 방향에 대한
        ny = y + dy[i] # 다음 위치의 좌푯값 설정
        # 조사 대상 범위를 애초부터 범위를 벗어나는 경우가 없도록 설정
        tmp += arr[nx][ny]
        # 모든 방향 조사 완료 후, 글로벌에 있는 최종 결과값보다 큰지 작은지 판별
    if tmp % 2 == 0:
        tmp = tmp * 2
    if result < tmp:
        result = tmp
T= int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0  # 최종 결과값
    '''
    보너스 점수에 해당하는 부분이 범위를 벗어나면 0점 처리
    '''
    for i in range(1, N-1): # 문제 조건상 불필요한 부분 제외
        for j in range(1, N-1):
            search(i, j)
    print(f'#{test_case} {result}')

### 나의 코드 ###
# T = int(input()) # 테스트 케이스 추출
# for test_case in range(1, T + 1):
#     N = int(input()) # 배열 갯수 추출
#     arr = [list(map(int, input().split())) for _ in range(N)] # 배열 추출
#
#     # print(T) # 3
#     # print(N) # 3
#     # print(arr) # [[1, 1, 1], [1, 5, 1], [1, 1, 1]]
#
#     di = [0, 1, 0, -1] # 상하좌우를 추출
#     dj = [1, 0, -1, 0]
#
#     max_gun = 0 # 보너스 점수 최댓값
#
#     for n1 in range(N): # N x N 배열
#         for n2 in range(N):
#             gun = arr[n1][n2] # 각 칸의 사격 점수
#             # print(gun) # 1 1 1 1 5 1 1 1 1
#
#             news = 0 # 상하좌우 값 추출
#             for k in range(4): # 상하좌우 위치
#                 x = n1 + di[k]
#                 y = n2 + dj[k]
#
#                 if 0 <= x < N and 0 <= y < N: # 배열에서 벗어나지 않도록 범위 지정
#                     news += arr[x][y]
#
#                 if max_gun < news: # 최댓값 추출
#                     max_gun = news
#
#     max_gun -= gun # 최댓값에서 해당하는 칸 빼기
#
#     if max_gun % 2 == 0:  # 만약 보너스 점수가 짝수면 두배가 된다
#         max_gun = max_gun * 2
#     else: # 보너스 점수가 홀수라면 그냥 출력한다
#         pass
#
#     if max_gun > 0:  # 만약 보너스 점수가 양수면 점수가 되고
#         pass
#     else:  # 보너스 점수가 음수면 0점이 된다
#         max_gun = 0
#
#     # 상하좌우 네 칸의 점수를 더한 값에서 맞힌 칸의 점수를 뺀다
#     print(f'#{test_case} {max_gun}')
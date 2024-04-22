import sys
sys.stdin = open('algo2_sample_in.txt')


def search(r, cnt):
    global result
    if r == N:              # 모든 행 조사를 마쳤다면
        if result < cnt:    # 최댓값 갱신
            result = cnt
    else:
        for k in range(N):  # r번째 행의 모든 열에 대해서
            # 아직 k번째 열을 조사해보지 않았고,
            # 해당 값이 양수이면 (음수인 경우 탈락이므로 고려 x)
            if not visited[k] and data[r][k] >= 0:
                visited[k] = 1  # r번째 행의 k번째 값을 사용했다고 작성하고,
                search(r+1, cnt + data[r][k])   # 누적값과 함께 다음 행 조사
                visited[k] = 0  # k번째 열을 사용하지 않고, r번째의 다음 열에 대해 조사하러 이동


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    visited = [0] * N       # 각 열마다 사용여부 판단
    search(0, 0)            # 0번행, 누적값 0부터 조사 시작
    print(f'#{tc} {result}')
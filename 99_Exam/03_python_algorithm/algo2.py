import sys
sys.stdin = open('algo2_sample_in.txt')

def search(x, y):
    tmp = -101      # 최솟값이 -100이므로 비교군 설정
    pos = []        # 최댓값의 좌표도 함께 반환 예정
    for i in range(x, x+M):
        for j in range(y, y+M):
            if i < N and j < N:         # 둘 다 범위를 벗어나지 않는 다면
                if tmp < data[i][j]:    # 최댓값, 좌표 갱신
                    tmp = data[i][j]
                    pos = [i, j]
    return tmp, pos # 해당 위치 반환

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    pos = [0, 0]
    stack = []

    while True:
        tmp, pos = search(pos[0], pos[1])   # 0, 0 에서 조사 시작한 뒤,
        if stack and pos == stack[-1]:      # 조사 결과가 이전과 같은 포지션이면
            break                           # 조사 중단
        result += tmp       # 그 외의 경우, 값 누적
        stack.append(pos)   # 좌푯값 stack에 저장

    print(f'#{tc} {result}')


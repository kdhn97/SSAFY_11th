import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    # 빨리 끝나는 사람들 먼저 시키도록 정렬
    data.sort(key=lambda x: x[1])
    # 누적 작업량
    result = 0
    # 비교군 비교군
    time = [0, 0]
    for d in data:  # 모든 시간에 대해
        if result == 0: # 첫 조사라면
            time = d    # 일단 삽입
            result += 1
        # 이번 신청자의 시작시간이 이전 신청자의 종료시간보다 크다면
        elif d[0] >= time[1]:   # 작업가능
            result += 1
            time = d            # 이번 신청자의 작업시간으로 갱신
    print(f'#{tc} {result}')

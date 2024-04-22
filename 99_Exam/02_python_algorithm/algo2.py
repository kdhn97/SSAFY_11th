import sys
sys.stdin = open('algo2_sample_in.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    data = list(map(int, input().split()))

    result = 0  # 최종 결괏값
    now = 0     # 점프 시작위치는 항상 제일 왼쪽 (리스트의 0번 인덱스)
    prev = 0    # 이전에 이동했었던 거리를 기록해 둘 필요가 있다.
    for _ in range(K):  # K번 만큼 점프한다. -> 몇번째 점프인지 중요하지 않음.
        next = data[now]  # 이동전, 이동해야 할 거리 기록
        # 한번 뒤로 갔다가, 앞으로 간다면
        if prev < 0 and data[now] >= 0:
            next += -prev
        prev = data[now]    # 이전번에 이동한만큼의 값 기록
        # 이동 코드
        now += next         # 이동!
        # 현재 위치가 범위를 벗어나면 종료
        # if 0 <= now < N: pass   # 뛸 수 있는 범위
        # else: break
        if now < 0 or now >= N: # 이동 후에, 범위 벗어났는지 조사
            break   # 범위를 벗어났으므로 종료
        result += data[now]

    print(f'#{tc} {result}')



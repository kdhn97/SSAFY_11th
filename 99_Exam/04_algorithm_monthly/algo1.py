import sys
sys.stdin = open('algo1_sample_in.txt')


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    '''
        rule = [[i₁, j₁, w₁], [i₂, j₂, w₂,]... ]
        w == 1 | i번째부터 j개의 돌 뒤집기
        w == 2 | i번째부터 j개의 돌을 i번째 돌 색으로
        w == 3 | i번째부터 대칭 j개의 돌이 같은색이면 뒤집기
    '''
    rule = [list(map(int, input().split())) for _ in range(M)]

    for r in rule:
        i, j, w = r
        i -= 1          # index 번호 -1
        origin_i = data[i]  # i번째 돌의 색
        while j:        # 뒤집을 횟수가 남은 동안
            if w == 1:  # 1번 룰 적용
                if 0 <= i + j - 1 < N:  # i = 3, j = 2, w = 1일때...
                    # i -> -1로 index 번호 맞춰짐 + j -> 2, 1 순으로 점점 작아질 예정
                    # j가 0이 되면 while은 종료되고, i번째 위치부터 j번 이므로
                    # i + 2, i + 1이 아닌, i + 1, i + 0에 대해서 돌 바꾸기
                    data[i+j-1] = 1 - data[i+j-1]
                    # 1 - 0 => 1
                    # 1 - 1 => 0
            elif w == 2:    # 2번 룰 적용
                if 0 <= i + j - 1 < N:
                    data[i+j-1] = origin_i  # 원본 돌로 바꾸기
            elif w == 3:    # 3번 룰 적용
                left = i - j    # i를 기준으로
                right = i + j
                if 0 <= left and right < N: # 범위 벗어나지 않고
                    if data[left] == data[right]:       # 좌우 대칭이면
                        data[left] = 1 - data[left]     # 뒤집기
                        data[right] = 1 - data[right]
            j -= 1  # 뒤집을 횟수 1 차감

    print(f'#{tc}', *data)


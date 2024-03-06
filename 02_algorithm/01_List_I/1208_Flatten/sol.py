import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))

    h_cnt = [0] * 101   # 높이 카운트 -> 100이라는 높이를 이용할 것이므로 101
    min_v = 101         # 최소, 최대 비교 대상 초기화
    max_v = 0

    # 박스의 높이를 카운트 하면서(h_cnt) 최고점과 최저점을 찾기
    for i in range(100):
        h_cnt[boxes[i]] += 1    # box의 높이가 1 -> 높이가 1인 박스의 수 1 증가

        # 최대, 최소 값 갱신
        if boxes[i] > max_v:
            max_v = boxes[i]
        if boxes[i] < min_v:
            min_v = boxes[i]

    # 덤프 횟수가 다했거나
    # 덤프 횟수는 남았지만 (최대 - 최소) 크기 차이가 1 이상인경우
    while dump > 0 and max_v - min_v > 1:
        # 평탄화를 한다 == 제일 높은 곳에서 제일 낮은 곳으로 박스를 하나 옮긴다.
        # 박스 높이가 1이었던 박스가 하나 적어진다
        # 박스 높이가 100이었던 박스가 하나 적어진다.
        h_cnt[min_v] -= 1
        h_cnt[max_v] -= 1

        # 박스 높이가 99인 박스가 하나 증가한다
        # 박스 높이가 2인 박스가 하나 증가한다
        h_cnt[min_v+1] += 1
        h_cnt[max_v-1] += 1

        # 지금 조사중인 제일 작은 박스가 더 이상 안남았다면
        # 다음 작은 박스로 조사 대사 이동
        if h_cnt[min_v] == 0:
            min_v += 1

        # 위와 동일
        if h_cnt[max_v] == 0:
            max_v -= 1

        # 한 번 덤프
        dump -= 1
    result = max_v - min_v
    print(f'#{tc} {result}')
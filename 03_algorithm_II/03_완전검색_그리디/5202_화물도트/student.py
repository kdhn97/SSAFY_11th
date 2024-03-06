import sys
sys.stdin = open('input.txt')

# 화물 도크
# 첫 줄에 테스트케이스의 수 T가 주어진다.
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())  # 첫 줄에 신청서 개수 N이 주어진다.
    field = [list(map(int, input().split())) for _ in range(N)]
    field.sort(key=lambda x: x[1])  # field 배열을 종료시간 순으로 정렬한다.
    # print(field)
    # 몇대의 화물차가 이용할 수있는지를 세줄 cnt와 종료시간을 나타낼 end
    cnt, end = 0, 0
    for i in range(N):  # 2차원 배열을 순회하면서
        s, e = field[i]  # s와 e에 각각 시작시간, 종료시간 저장
        if end <= s:  # 시작시간이 직전 종료시간보다 크거나 같으면
            end = e  # 종료시간을 업데이트
            cnt += 1  # cnt +1
    print(f'#{test_case} {cnt}')
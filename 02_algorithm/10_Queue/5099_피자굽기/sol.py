import sys
sys.stdin = open('input.txt')


# 테스트케이스 입력
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())       # 화덕의 크기 N, 피자 개수 M
    # 파이썬에 조금 더 익숙했더라면
    Ci = [[idx, int(ci)] for idx, ci in enumerate(input().split(), 1)]
    # 피자 선입 선출
    oven = [Ci.pop(0) for _ in range(N)]  # 오븐의 크기만큼
    while len(oven) != 1:
        pizza = oven.pop(0)
        pizza[1] //= 2
        if pizza[1]:    # 치즈 남았으면 (0이 아니면)
            oven.append(pizza)  # 피자 다시 넣기
        elif pizza[1] == 0 and Ci:  # 이번 피자는 치즈 다 녹았는데,
            # 더 넣어야 할 피자 목록 (Ci)이 남았다면
            oven.append(Ci.pop(0))
    print(f'#{tc} {oven[0][0]}')



import sys
sys.stdin = open('input.txt')

# 테스트케이스 입력
T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())       # 화덕의 크기 N, 피자 개수 M
    Ci = list(map(int, input().split()))   # 피자 치즈의 양 Ci

    # firepit : 화덕 내 피자 정보
    # 초기값은 피자 M 개중 N 개로 설정
    firepit = [[0, 0] for _ in range(N)]
    for i in range(N):
        firepit[i][0] = i + 1
        firepit[i][1] = Ci[i]

    # Cheese : 화덕에 들어가지 못하고 대기중인 피자 정보
    # 초기값은 firepit 초기 설정하고 남은 피자 (M - N)개로 설정
    Cheese = [[0,0] for _ in range(M - N)]
    for i in range(N, M):
        Cheese[i - N][0] = i + 1
        Cheese[i - N][1] = Ci[i]

    # 화덕에 피자가 1개 남을때까지 반복
    while len(firepit) > 1:

        # 1번위치(index 0)의 피자 치즈 확인
        # 기존의 양 //2
        firepit[0][1] //= 2

        # 확인했는데 치즈의 양이 0이면 화덕에서 꺼내고
        # 대기 중인 피자가 있다면 빈 자리에 투입
        if firepit[0][1] == 0:
            firepit.pop(0)
            if Cheese != []:
                firepit.append(Cheese.pop(0))
                # firepit.insert(0, Cheese[0])
                # Cheese.pop(0)
                # turn = firepit.pop(0)
                # firepit.append(turn)
            # else:
            #     pass
        else:
            # 다음 피자 확인을 위해 화덕 회전
            turn = firepit.pop(0)
            firepit.append(turn)

    print(f'#{t} {firepit[0][0]}')


'''
오답 >> 화덕에 더 이상 넣을 피자가 없을 때 한번 더 불필요한 회전이 발생

import sys
sys.stdin = open('5099_im_input.txt')

# 테스트케이스 입력
T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())       # 화덕의 크기 N, 피자 개수 M
    Ci = list(map(int, input().split()))   # 피자 치즈의 양 Ci

    # firepit : 화덕 내 피자 정보
    # 초기값은 피자 M 개중 N 개로 설정
    firepit = [[0, 0] for _ in range(N)]
    for i in range(N):
        firepit[i][0] = i + 1
        firepit[i][1] = Ci[i]

    # Cheese : 화덕에 들어가지 못하고 대기중인 피자 정보
    # 초기값은 firepit 초기 설정하고 남은 피자 (M - N)개로 설정
    Cheese = [[0,0] for _ in range(M - N)]
    for i in range(N, M):
        Cheese[i - N][0] = i + 1
        Cheese[i - N][1] = Ci[i]

    print(firepit)
    print(Cheese)

    # 화덕에 피자가 1개 남을때까지 반복
    while len(firepit) > 1:

        # 1번위치(index 0)의 피자 치즈 확인
        # 기존의 양 //2
        firepit[0][1] //= 2

        # 확인했는데 치즈의 양이 0이면 화덕에서 꺼내고
        # 대기 중인 피자가 있다면 빈 자리에 투입
        if firepit[0][1] == 0:
            firepit.pop(0)
            if Cheese != []:
                firepit.insert(0, Cheese[0])
                Cheese.pop(0)

        # 다음 피자 확인을 위해 화덕 회전
        turn = firepit.pop(0)
        firepit.append(turn)

    print(f'#{t} {firepit[0][0]}')
'''
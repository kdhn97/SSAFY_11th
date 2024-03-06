for test_case in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total = 0 # 교착 상태 횟수
    for i in range(N):
        flag = 0 # 교착 상태
        for j in range(N):
            if arr[j][i] == 1: # 세로 1 확인
                flag = 1
            elif arr[j][i] == 2: # 세로 2 확인
                if flag: # flag가 1이라면
                    total += 1 # 교착 횟수 증가
                    flag = 0 # 교착 상태 초기화
    print(f'#{test_case} {total}')
'''
#1 471
#2 446
'''
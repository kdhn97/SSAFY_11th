import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    result = []

    #배열 입력 받기
    arr = []
    for _ in range(N):
        arr.append(input())

    #가로 검색
    for row in range(N):
        for col in range(N - M + 1):
            # 회문이 맞는지 확인
            if arr[row][col:col+M] == arr[row][col:col+M][::-1]:
                # 회문이면 결과 리스트에 추가
                result.append(arr[row][col:col+M])
    #세로 검색
    for row in range(N - M + 1):
        for col in range(N):
            col_list = [] # 새로 열 리스트를 만들어주기
            for i in range(M):
                col_list.append(arr[row+i][col])
            if col_list == col_list[::-1]: # 세로줄이 회문이면
                result.append(''.join(col_list)) # 결과리스트에 추가.

    print(f'#{test_case} {result[0]}')
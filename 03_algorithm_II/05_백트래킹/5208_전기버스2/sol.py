import sys
sys.stdin = open('input.txt')

def func(s):
    global cnt
    for j in range(s): # 갈 수 있는 범위의 정류장 추출
        arr.append(station[j])
    for k in range(len(arr)):
        if arr[k] >= N: # 목적지까지 갈 수 있는 범위가 있다면
            cnt += 1 # 해당 범위를 간 뒤
            return
    # 목적지까지 갈 수 있는 범위가 없다면
    cnt += 1
    func(max(arr)) # 범위 중 가장 큰 값

T = int(input())
for test_case in range(1, T+1): # test_case: 1
    N, *M = list(map(int, input().split())) # N: 5, M: [2, 3, 1, 1]
    station = [] # 각 정류장에서 갈 수 있는 최대 정류장
    for i in range(len(M)):
        station.append(i+1+M[i]) # station = [3, 5, 4, 5]
    cnt = 0 # 교환 횟수
    arr = [] # 갈 수 있는 범위의 정류장
    func(station[0]) # 1번에서 출발
    print(f'#{test_case} {cnt}') #1 1
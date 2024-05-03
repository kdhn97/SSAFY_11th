import sys
sys.stdin = open('input.txt')

def func(n):
    if n == 0:
        return
    for i in range(len(serial)):
        if i + 1 < n:
            # 조건 1. A와 B의 길이가 다르면, 짧은 것이 먼저 온다.
            if len(serial[i][0]) != len(serial[i+1][0]):
                if len(serial[i][0]) > len(serial[i+1][0]):
                    serial[i][0], serial[i+1][0] = serial[i+1][0], serial[i][0]
            # 조건 2. 만약 서로 길이가 같다면, A의 모든 자리수의 합과 B의
            # 모든 자리수의 합을 비교해서 작은 합을 가지는 것이 먼저온다. (숫자인 것만 더한다)
            elif len(serial[i][0]) == len(serial[i+1][0]):
                back_num = 0
                front_num = 0
                for j in range(len(serial[i][0])):
                    if serial[i][0][j].isdigit(): # 숫자인 것만 판별
                        back_num += int(serial[i][0][j])
                    if serial[i+1][0][j].isdigit(): # 숫자인 것만 판별
                        front_num += int(serial[i+1][0][j])
                if back_num > front_num:
                    serial[i][0], serial[i+1][0] = serial[i+1][0], serial[i][0]
                # 조건 3. 만약 1,2번 둘 조건으로도 비교할 수 없으면, 사전순으로 비교한다.
                # 숫자가 알파벳보다 사전순으로 작다.
                if back_num == front_num:
                    answer = [serial[i][0], serial[i+1][0]]
                    answer.sort()
                    serial[i][0] = answer[0]
                    serial[i+1][0] = answer[1]
    func(n-1)

N = int(input()) # 기타의 개수
serial = [input().split() for _ in range(N)] # 시리얼 번호
func(N) # 기타의 개수만큼 반복해서 비교
for s in range(len(serial)): # 최종 시리얼 번호 출력
    print(serial[s][0])
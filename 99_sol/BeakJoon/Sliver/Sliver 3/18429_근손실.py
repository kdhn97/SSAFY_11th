import sys
sys.stdin = open('input.txt')

from itertools import permutations

def func(n, m):
    global weight, cnt

    for i in range(len(per_num)): # 조합갯수만큼
        for j in range(n): # n일만큼
            weight -= m # 매일 m만큼 감소
            weight += per_num[i][j] # 중량만큼 증가
            if weight < 500: # 중량이 500이하면
                break # 끝
        if weight > 500: # 중량이 500보다 크면
            cnt += 1 # 가능 횟수 증가
        weight = 500 # 중량 초기화
    return

N, M = map(int, input().split())
num = list(map(int, input().split()))
per_num = list(permutations(num, N)) # 조합 생성
weight = 500 # 현재 중량
cnt = 0 # 가능 횟수
func(N, M)
print(cnt)
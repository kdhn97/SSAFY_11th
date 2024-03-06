import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 오름차순 정렬
    W = sorted(list(map(int, input().split())))
    T = sorted(list(map(int, input().split())))
    result = 0
    while W and T:  # 화물이든 트럭이든 남은동안
        # 무거운것부터 조사
        if T[-1] >= W[-1]:  # 트럭이 화물 감당 가능하면
            result += W[-1] # 제일 무거운 화물 추가
            # 화물 싣고 출발
            W.pop()
            T.pop()
        else:               # 제일 큰 트럭이 감당 못하면
            W.pop()         # 갖다버림

    print(f'#{tc} {result}')
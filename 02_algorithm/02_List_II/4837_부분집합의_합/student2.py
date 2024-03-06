from itertools import combinations
import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    # 1부터 12까지를 원소로 가진 집합 A
    A = {i for i in range(1, 13)}
    # N개 원소, 원소의 합 K
    N, K = map(int, input().split())
    # 원소가 3개인 부분집합을 전부 배열에 저장
    booboon = []
    booboon += list(combinations(A, N))
    # count 0으로 초기화
    count = 0
    # 각각의 부분집합의 합이 K와 같으면 count + 1
    for boo in booboon:
        if sum(boo) == K:
            count += 1
    # 테케와 결과 같이 출력
    print(f'#{test_case} {count}')
    print(booboon)
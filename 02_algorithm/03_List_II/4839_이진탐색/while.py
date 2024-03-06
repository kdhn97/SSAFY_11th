import sys
sys.stdin = open('input.txt')

def binary_search_while(start, end, target, cnt):
    # 중간 위치 인덱스번호
    middle = (start + end) // 2
    # middle 번째 값이 내가 찾는 target이 아닌동안
    while middle != target:
        if middle > target:
            end = middle
        elif middle < target:
            start = middle
        middle = (start + end) // 2
        cnt += 1    # 조사했는데 못찾음.. .한 번 더 조사해야함..
    return cnt
T = int(input())

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    # start = 0, end = P, target = Pa, count= = 0
    result_A = binary_search_while(1, P, Pa, 0)
    result_B = binary_search_while(1, P, Pb, 0)

    if result_A < result_B:
        print('A')
    elif result_A > result_B:
        print('B')
    else:
        print(0)
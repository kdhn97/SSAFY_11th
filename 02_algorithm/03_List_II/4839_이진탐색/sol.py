import sys
sys.stdin = open('input.txt')

def binary_search(start, end, target, cnt):
    # 중간 위치 인덱스 번호
    middle = (start + end) // 2
    # 언제까지? 중간지점이 내가 찾는 대상이면
    if middle == target:
        return cnt
    else:   # 아니면 조사
        if middle > target:
            return binary_search(start, middle, target, cnt+1)
        else:
            return binary_search(middle, end, target, cnt+1)

T = int(input())

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    # start = 0, end = P, target = Pa, count= = 0
    result_A = binary_search(1, P, Pa, 0)
    result_B = binary_search(1, P, Pb, 0)

    if result_A < result_B:
        print('A')
    elif result_A > result_B:
        print('B')
    else:
        print(0)
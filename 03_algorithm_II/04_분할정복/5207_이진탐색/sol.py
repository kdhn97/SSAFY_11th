import sys
sys.stdin = open("input.txt")

def binary_search(target, direction):
    global cnt
    left = 0
    right = len(A) - 1

    while left <= right:
        m = (left + right) // 2
        # 찾았다면 개수 증가
        if A[m] == target:
            cnt += 1
            return
        # 왼쪽 부분은 direction 1
        elif A[m] > target:
            if direction == 1:
                return
            right = m - 1
            direction = 1
        # 오른쪽 부분은 direction 2
        elif A[m] < target:
            if direction == 2:
                return
            left = m + 1
            direction = 2
    return

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0
    for i in B:
        # B 리스트 요소 이진 탐색
        binary_search(i, 0)
    print(f'#{test_case}', cnt)
import sys
sys.stdin = open('input.txt')


def divide_conquer(start, end):
    if start == end:
        return start
    middle = (start + end) // 2
    left = divide_conquer(start, middle)
    right = divide_conquer(middle + 1, end)


    winner = (arr[left] - arr[right]) % 3
    if winner == 2:
        return right
    else:
        return left

    # if left[0] == 1 and right[0] == 2:
    #     return right
    # elif left[0] == 2 and right[0] == 3:
    #     return right
    # elif left[0] == 3 and right[0] == 1:
    #     return right
    # return left

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 가위 1 바위 2 보 3
    arr = list(map(int, input().split()))

    result = divide_conquer(0, N-1)
    print(f'#{tc} {result + 1}')
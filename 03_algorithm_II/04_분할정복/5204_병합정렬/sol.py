import sys
sys.stdin = open('input.txt')

def merge_sort(arr): # 분할 과정
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2  # 중간값
    left = [] # mid의 왼쪽값
    right = [] # mid의 오른쪽값
    for i in arr[:mid]:
        left.append(i)
    for j in arr[mid:]:
        right.append(j)
    left_lst = merge_sort(left)
    right_lst = merge_sort(right)
    return merge(left_lst, right_lst)

def merge(left, right): # 병합 과정
    global cnt
    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수
    if left[-1] > right[-1]:
        cnt += 1
    result = []

    i = j = 0
    # 왼쪽과 오른쪽에 요소가 있다면
    while len(left) > i and len(right) > j:
        # 값을 비교하여 작은 것을 삽입
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # 한 쪽만 남았다면 그대로 result에 삽입
    while len(left) > i:
        result.append(left[i])
        i += 1
    while len(right) > j:
        result.append(right[j])
        j += 1
    return result

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split())) # [2, 2, 1, 1, 3]
    cnt = 0
    answer = merge_sort(A) # answer에 할당해주어야 한다
    print(f'#{test_case} {answer[N//2]} {cnt}') # #1 2 0
import sys
sys.stdin = open('input.txt')

def quick(arr, left, right): # arr: [2, 2, 1, 1, 3], left: 0, right: 4
    if left < right: # 시작점과 끝점이 교차하지 않았다면
        mid = partition(arr, left, right)
        quick(arr, left, mid-1) # pivot 기준 왼쪽 값 정렬
        quick(arr, mid, right) # pivot 기준 오른쪽 값 정렬

def partition(arr, left, right):
    # 문제의 원인 : arr[N//2] -> 피벗을 배열의 중간값으로 선택
    pivot = arr[(left + right) // 2] # pivot: 1 = arr[2]
    while left <= right:
        while arr[left] < pivot:
            left += 1 # p보다 큰 값을 만날때까지
        while arr[right] > pivot:
            right -= 1 # p보다 작은 값을 만날때까지
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left, right = left + 1, right - 1
    return left # 중간값

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split())) # [2, 2, 1, 1, 3]
    quick(A, 0, N-1)
    print(f'#{test_case} {A[N//2]}')
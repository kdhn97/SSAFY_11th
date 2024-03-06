import sys
sys.stdin = open('input.txt')

def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

for tc in range(1, 11):
    dump = int(input())
    matrix = list(map(int, input().split()))

    bubble_sort(matrix) # 정렬 한다
    while dump:         # 덤프 가능한 동안 반복
        matrix[0] += 1
        matrix[-1] -= 1
        bubble_sort(matrix)
        dump -= 1

    print(f'#{tc} {matrix[-1] - matrix[0]}')





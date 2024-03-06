import sys
sys.stdin = open('input.txt')

def counting_sort():
    counting_arr = [0] * 101
    sorted_ai = [0] * N
    for num in ai:
        counting_arr[num] += 1

    for index in range(1, 101):
        counting_arr[index] += counting_arr[index - 1]

    for index in range(N):
        sorted_ai[counting_arr[ai[index]]-1] = ai[index]

    for i in range(N//2):
        result[i*2] = sorted_ai[len(sorted_ai) - 1 - i]
        result[i*2+1] = sorted_ai[i]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))
    result = [0] * N
    counting_sort()

    print(f'#{tc}', *result[:10])
import sys
sys.stdin = open('input.txt')

T = int(input()) # 테스트 케이스
for test_case in range(1, T + 1):
    N = int(input()) #  배열의 길이 3
    arr = list(map(int, input().split())) # 배열 [3, 5, 9]

    result = 0 # 총 판매액 (9-5=4) + (9-3=6) -> 10
    max_arr = arr[-1] # 최댓값 9
    for i in range(N-1,-1,-1): # 뒤에서부터 확인 9 -> 5 -> 3
        if arr[i] > max_arr: # arr[i] : 9 > max_arr : 9
            max_arr = arr[i] # max_arr : 9
        result += max_arr - arr[i]
        # 5 < 9이므로 9 - 5 = 4
        # 3 < 9이므로 9 - 3 = 6

    print(f'#{test_case} {result}')
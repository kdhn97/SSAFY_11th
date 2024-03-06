import sys
sys.stdin = open('input.txt')

T = 10
for test_case in range(1, T+1):

    dump = int(input())
    height = list(map(int, input().split()))

    while dump > 0: # 덤핑이 0보다 큰 동안
        max_height = height.index(max(height)) # 추가
        min_height = height.index(min(height)) # 추가

        height[max_height] -= 1 # 가장 큰 높이에서 1씩 빼기
        height[min_height] += 1 # 가장 낮은 높이에서 1씩 추가
        dump -= 1 # 덤프를 하나씩 차감

    if max(height) - min(height) <= 1: # 만약 덤프가 남았는데 가장 큰 높이와 낮은 높이의 차가 1이하라면
        break # 종료

    result = max(height) - min(height) # 최종 큰 높이 - 낮은 높이 산출
    print(f'#{test_case} {result}')
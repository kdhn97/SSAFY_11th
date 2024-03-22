import sys
sys.stdin = open('input.txt')

def dfs(cnt, sum_height):
    global answer
    # 기저조건
    # 1. 키의 합이 B 이상이면 종료 -> 현재까지 쌓은 탑의 높이
    if sum_height >= B:
        # 제일 높이가 낮은 탑이 정답
        # -> 최소 탑의 높이는 재귀호출함수들이 '동시에' 사용함
        answer = min(answer, sum_height)
        return
    # 2. 모든 점원이 탑을 쌓았다면 종료 -> 현재까지 쌓은 점원의 수
    if cnt == N:
        return
    # 재귀호출파트
    dfs(cnt+1, sum_height + arr[cnt]) # 쌓는다
    dfs(cnt+1, sum_height)            # 안 쌓는다

T = int(input())
for test_case in range(1, T+1):
    N, B = map(int, input().split()) # 5 16
    arr = list(map(int, input().split())) # 1 3 3 5 6
    answer = int(1e9)
    dfs(0, 0)
    print(f'#{test_case} {abs(answer - B)}') # #1 1
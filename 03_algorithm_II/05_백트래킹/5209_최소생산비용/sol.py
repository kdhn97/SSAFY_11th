import sys
sys.stdin = open('input.txt')

def func(idx, total): # idx: 현재 행, total: 현재 원소의 합
    global min_v
    if idx == N: # 모든 행을 돌았다면
        if min_v > total: # total이 작으면
            min_v = total # min_v를 total로 교체
    elif total >= min_v: # total이 min_v보다 크면
        return # 볼 필요 없으니 거른다
    for i in range(N):
        if i not in visited: # 방문하지 않았다면
            visited.append(i)
            func(idx+1, total+arr[idx][i])
            # 방문 기록을 pop을 해줘야 다른 i값으로 돌릴 수 있음.
            visited.pop()

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [] # 방문한 열
    min_v = 1000
    func(0, 0)
    print(f'#{test_case} {min_v}')
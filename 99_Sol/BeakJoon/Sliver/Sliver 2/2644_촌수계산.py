import sys
sys.stdin = open('input.txt')

def func(n, m):
    global cnt, result
    if result == False:
        if n == m: # 촌수가 같다면
            result = True # 제한 조건을 True 변경
            print(cnt)
            return
    if result == False:
        for i in range(len(arr[n])):
            if visited[arr[n][i]] == True: # 방문했다면
                continue
            cnt += 1
            visited[arr[n][i]] = True # 방문 처리
            func(arr[n][i], m)
            cnt -= 1 # 갈 곳이 없다면 카운트 - 1

human = int(input()) # 전체 사람의 수 : 9
N, M = map(int, input().split()) # 계산해야 할 촌수 : 7, 3
node = int(input()) # 부모 자식 관계 개수 : 7
tree = [list(map(int, input().split())) for _ in range(node)]
visited = [False] * (human+1) # 방문 처리
result = False # 제한 조건
cnt = 0 # 촌수 count
arr = [[] for _ in range(human+1)]
for i in range(node):
    [n1, n2] = tree[i]
    arr[n1].append(n2)
    arr[n2].append(n1)
# print(arr) # [[], [2, 3], [1, 7, 8, 9], [1], [5, 6], [4], [4], [2], [2], [2]]
func(N, M)
if result == False: # 최종적으로 조건에 걸리는게 없으면
    print(-1)

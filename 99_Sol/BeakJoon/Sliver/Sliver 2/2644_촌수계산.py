import sys
sys.stdin = open('input.txt')

def func(n, m):
    global cnt, result

    if result == False:
        if m in arr[n]:
            cnt += 1
            result = True
            print(cnt)
            return

    if result == False:
        for i in range(len(arr[n])):
            cnt += 1
            func(arr[n][i], m)


human = int(input())
N, M = map(int, input().split())
node = int(input())
tree = [list(map(int, input().split())) for _ in range(node)]
result = False
cnt = 0

arr = [[] for _ in range(human+1)]

for i in range(node):
    [n1, n2] = tree[i]
    arr[n1].append(n2)
    arr[n2].append(n1)

# print(arr) # [[], [2, 3], [1, 7, 8, 9], [1], [5, 6], [4], [4], [2], [2], [2]]
func(N, M)
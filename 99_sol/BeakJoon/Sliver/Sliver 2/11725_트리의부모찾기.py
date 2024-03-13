import sys
sys.stdin = open('input.txt')

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = (map(int, input().split()))
    tree[a] += [b]
    tree[b] += [a]
# [[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]]
for i in range(2, len(tree)):
    print(tree[i][0])
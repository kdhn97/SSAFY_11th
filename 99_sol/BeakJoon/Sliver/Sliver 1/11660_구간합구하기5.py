import sys
sys.stdin = open('input.txt')

N, M = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]
sol = [list(map(int, input().split())) for _ in range(M)]

xy = [] # [[2, 2], [3, 4], [3, 4], [3, 4], [1, 1], [4, 4]]
for s in range(M):
    xy.append(sol[s][0:2])
    xy.append(sol[s][2:4])


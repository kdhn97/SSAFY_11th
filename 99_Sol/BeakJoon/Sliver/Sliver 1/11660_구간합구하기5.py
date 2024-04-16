import sys
sys.stdin = open('input.txt')

N, M = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]
sol = [list(map(int, input().split())) for _ in range(M)]

xy = [] # [[2, 2], [3, 4], [3, 4], [3, 4], [1, 1], [4, 4]]
for s in range(M):
    xy.append(sol[s][0:2])
    xy.append(sol[s][2:4])

result = []
for i in range(len(xy)//2):
    cnt = 0
    x1 = xy[i*2][0]
    x2 = xy[i*2+1][0]
    y1 = xy[i*2][1]
    y2 = xy[i*2+1][1]
    for j in range(x1-1, x2):
        for k in range(y1-1, y2):
            cnt += arr[j][k]
    result.append(cnt)

for r in range(len(result)):
    print(result[r])
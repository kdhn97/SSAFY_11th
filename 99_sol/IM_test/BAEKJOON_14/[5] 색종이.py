paper = int(input())
num = [list(map(int, input().split())) for _ in range(paper)]

arr = [[0] * 101 for _ in range(101)]

for p in range(paper):
    for i in range(10):
        for j in range(10):
            arr[num[p][0]+i][num[p][1]+j] = 1

one = 0
for k in range(101):
    one += arr[k].count(1)
print(one) # 260
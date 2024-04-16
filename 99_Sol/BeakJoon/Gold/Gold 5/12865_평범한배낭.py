import sys
sys.stdin = open('input.txt')

def func(i, k):
    global answerwer
    result = []
    if i == k:
        for j in range(k):
            if bit[j]:
                result.append(item[j])
    else:
        for j in range(2):
            bit[i] = j
            func(i+1, k)
    sum_w = 0
    sum_v = 0
    for r in range(len(result)):
        sum_w += result[r][0]
        sum_v += result[r][1]
    answer.append([sum_w, sum_v])

N, K = map(int, input().split())
item = [list(map(int, input().split())) for _ in range(N)]
answer = []
sol = []
bit = [0] * N
func(0, N)

for a in range(len(answer)):
    if answer[a][0] != 0 and answer[a][0] <= K:
        sol.append(answer[a])

max_v = 0
for i in range(len(sol)):
    if sol[i][1] > max_v:
        max_v = sol[i][1]

print(max_v)
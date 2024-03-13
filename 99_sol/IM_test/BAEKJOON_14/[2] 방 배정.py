# 학생 수: N, 최대 배정 인원 : K
N , K = map(int, input().split())
cnt = [[0]*6 for _ in range(2)]
result = 0

for _ in range(N):
    sex, grade  = map(int, input().split())
    cnt[sex][grade-1] += 1

for i in cnt:
    for j in i:
        if j % K == 0:
            result += j//K
        else:
            result += (j//K) + 1
print(result) # 3
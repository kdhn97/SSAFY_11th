import sys
sys.stdin = open("input.txt")

from itertools import * # 순열 라이브러리

num, count = list(map(int, input().split()))
N = []
for n in range(1, num+1):
    N.append(n)
# 순열 (permutations)
permut = list(permutations(N, count))

answer = [] # 중복된 순열
for p in range(len(permut)):
    answer.append(sorted(permut[p]))

result = [] # 중복을 제거한 순열
for a in range(len(answer)):
    if answer[a] not in result:
        result.append(answer[a])

for r in range(len(result)):
    print(*result[r])
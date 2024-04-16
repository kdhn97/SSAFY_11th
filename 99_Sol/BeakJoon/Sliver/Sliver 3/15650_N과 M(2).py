import sys
sys.stdin = open("input.txt")

from itertools import * # 순열 라이브러리

num, count = list(map(int, input().split()))
N = []
for n in range(1, num+1):
    N.append(n)
# print(N) # [1, 2, 3, 4]

permut = list(permutations(N, count)) # 순열 (permutations)
# print(permut) [(1,), (2,), (3,)]

answer = [] # 중복된 순열
for p in range(len(permut)):
    answer.append(sorted(permut[p]))
# print(answer) # [[1, 2], [1, 3], [1, 4], [1, 2], [2, 3], [2, 4], [1, 3], [2, 3], [3, 4], [1, 4], [2, 4], [3, 4]]

result = [] # 중복을 제거한 순열
for a in range(len(answer)):
    if answer[a] not in result:
        result.append(answer[a])
# print(result) # [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

for r in range(len(result)):
    print(*result[r])
'''
1 2
1 3
1 4
2 3
2 4
3 4
'''
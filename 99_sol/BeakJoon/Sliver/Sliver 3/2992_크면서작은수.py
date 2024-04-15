import sys
sys.stdin = open('input.txt')

from itertools import permutations # 조합

N = list(input())
perm = list(permutations(N, len(N)))

result = []

for i in range(len(perm)):
    perm_num = ''.join(perm[i])
    # 조합된 값이 입력값보다 크다면
    if int(perm_num) > int(''.join(N)): 
        result.append(int(perm_num))

if len(result) == 0: # 조건에 맞는 숫자가 없다면
    print(0)
else:
    print(min(sorted(result))) # 가장 작은 값
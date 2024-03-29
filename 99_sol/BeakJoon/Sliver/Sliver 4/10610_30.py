import sys
sys.stdin = open('input.txt')

from itertools import permutations

N = input()
lst = []
for n in permutations(N):
    join_n = int(''.join(n))
    if join_n % 30 == 0:
        lst.append(join_n)
if len(lst) == 0:
    print(-1)
else:
    print(max(lst))
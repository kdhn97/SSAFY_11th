import sys
sys.stdin = open('input.txt')

from itertools import permutations # 조합

N, M = map(int, input().split())
num = list(map(int, input().split()))
# 조합 생성 후 오름차순 정렬
per_num = sorted(list(permutations(num, M)))
# 각 조합 값을 출력
for i in range(len(per_num)):
    print(*per_num[i])
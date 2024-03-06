import sys
sys.stdin = open('input.txt')

def min_max():
    DESC_ASC = 'DESC'   # 첫 정렬 -> DESC
    for i in range(N):
        max_value = ai[i]
        max_idx = i
        min_value = ai[i]
        min_idx = i
        for j in range(i + 1, N): # 내 다음 위치랑 나랑 비교
            if max_value < ai[j]:
                max_value = ai[j]
                max_idx = j
            if min_value > ai[j]:
                min_value = ai[j]
                min_idx = j
        if DESC_ASC == 'DESC':
            ai[i], ai[max_idx] = ai[max_idx], ai[i]
            DESC_ASC = 'ASC'
        else:
            ai[i], ai[min_idx] = ai[min_idx], ai[i]
            DESC_ASC = 'DESC'



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))

    min_max()
    print(ai)
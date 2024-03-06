import sys
sys.stdin = open('input.txt')

def selection_sort():
    for x in range(10):
        mIdx = x
        for y in range(x + 1, N):
            if x % 2:
                if ai[mIdx] > ai[y]:
                    mIdx = y
            else:
                if ai[mIdx] < ai[y]:
                    mIdx = y
        ai[x], ai[mIdx] = ai[mIdx], ai[x]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))

    selection_sort()
    # result = ' '.join(map(str, ai[:10]))
    print(f'#{tc}', *ai[:10])


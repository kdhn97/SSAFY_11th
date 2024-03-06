import sys
sys.stdin = open('input.txt')

def bubble_sort():
    for i in range(N-1, 0, -1):
        for j in range(i):
            if i % 2:
                if ai[j] > ai[j + 1]:
                    ai[j], ai[j + 1] = ai[j + 1], ai[j]
            else:
                if ai[j] < ai[j + 1]:
                    ai[j], ai[j + 1] = ai[j + 1], ai[j]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))
    bubble_sort()
    ai.reverse()
    print(f'#{tc}', *ai[:10])
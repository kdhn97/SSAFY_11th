import sys
sys.stdin = open('algo1_sample_in.txt')


T = int(input())

for tc in range(1, T+1):
    N, data = input().split()
    # print(N, data)
    if N == '24':   # 2진수 -> 16진수
        print(f'#{tc} {int(data, 2):06X}')
    else:           # 16진수 -> 2진수
        print(f'#{tc} {int(data, 16):024b}')
import sys
sys.stdin = open('input.txt')

N = int(input())

for j in range(N, 1, -1):
    print((N-j) * ' ' + (j * 2 - 1) * '*')

for i in range(1, N+1):
    print((N-i) * ' ' + (i * 2 - 1) * '*')
import sys
sys.stdin = open('input.txt')

N = int(input())

result_five = []
result_three = []

result_five.append(N//5)
N = N % 5
result_three.append(N//3)
N = N % 3

if N == 0:
    print(N)
else:
    print(-1)
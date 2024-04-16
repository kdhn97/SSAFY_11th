import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))

a = len(sorted(set(arr)))
print(a)
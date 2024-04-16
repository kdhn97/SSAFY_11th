'''
2
3
1 5 3
1 1 0
4
1 5 3 2
1 1 1
'''

import sys
sys.stdin = open('input.txt')

def func(idx, arr, add, sub, mul):
    global min_num, max_num
    if idx == N:
        max_num = max(max_num, arr)
        min_num = min(min_num, arr)
        return
    if add:
        func(idx+1, arr+int_arr[idx], add-1, sub, mul)
    if sub:
        func(idx+1, arr-int_arr[idx], add, sub-1, mul)
    if mul:
        func(idx+1, arr*int_arr[idx], add, sub, mul-1)

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    int_arr = list(map(int, input().split()))
    Add, Sub, Mul = map(int, input().split())
    min_num, max_num = -10**10, 10**10
    func(1, int_arr[0], Add, Sub, Mul)
    print(min_num, max_num)

'''
-1 3
-10 16
'''
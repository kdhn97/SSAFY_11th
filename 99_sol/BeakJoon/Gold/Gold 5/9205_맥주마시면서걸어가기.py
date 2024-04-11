import sys
sys.stdin = open('input.txt')

def func(s, e):
    global result
    if result:
        return
    if abs(s[0] - e[0]) + abs(s[1] - e[1]) <= 1000:
        result = True
        return

    for i in range(len(arr)):
        if abs(s[0] - arr[i][0]) + abs(s[1] - arr[i][1]) <= 1000 and visited[i] == 0:
            visited[i] = 1
            s[0] = arr[i][0]
            s[1] = arr[i][1]
            func(s, e)
            visited[i] = 0
        else:
            print('sad')
            return

T = int(input())
for test_case in (1, T+1):
    N = int(input())
    result = False
    start = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    end = list(map(int, input().split()))
    visited = [0] * len(arr)
    func(start, end)
    if result:
        print('happy')
    else:
        print('sad')

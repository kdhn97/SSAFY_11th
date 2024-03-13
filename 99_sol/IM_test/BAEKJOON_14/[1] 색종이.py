T = int(input())
arr = [[0] * 100 for _ in range(1, 101)] # 100 * 100 격자
for t in range(T):
    x, y, width, high = map(int, input().split())

    for i in range(x, x+width): # 행의 길이
        for j in range(y, y+high): # 열의 길이
            arr[i][j] = t+1 # 색종이 순서를 좌표에 추가하기

for t in range(T):
    cnt = 0
    for a in arr:
        cnt += a.count(t+1)
    print(cnt)
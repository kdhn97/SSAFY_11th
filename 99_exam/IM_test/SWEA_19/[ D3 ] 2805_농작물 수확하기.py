T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    num = [input() for _ in range(N)]

    a = []
    for i in range(N):
        a.append(num[i][N//2-i:N//2+i+1])
        if i == N//2: # 중간 지점을 만나면
            for j in range(1,N-N//2):
                a.append(num[N//2+j][j:N-j])
            break
    d = []
    for b in range(N):
        for c in range(N):
            if 0<=c<len(a[b]):
                d.append(a[b][c])
    e = sum(map(int, d))
    print(f'#{test_case} {e}') # #1 23
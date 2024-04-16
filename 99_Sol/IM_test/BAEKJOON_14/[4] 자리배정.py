C,R = map(int,input().split())
seat = int(input())
arr = [[0] * C for _ in range(R)]

direct = x = y = 0
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 좌석을 줄 수 없는 경우
if seat > C * R :
    print(0)
    exit()

#행렬 돌면서
for s in range(1, C*R+1) :
    # 내 자리면 끝내기
    if s == seat:
        print(y+1, x+1)
        break
    else :
        # 표시하고
        arr[x][y] = s
        # 앞으로 전진
        x += dx[direct]
        y += dy[direct]

        if x<0 or y<0 or x>=R or y>=C or arr[x][y]:
            x -= dx[direct]
            y -= dy[direct]
            # 범위 벗어나면 방향 바꿔서 전진
            direct = (direct+1) % 4
            x += dx[direct]
            y += dy[direct]
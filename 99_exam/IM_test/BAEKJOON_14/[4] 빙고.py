bingo = [list(map(int, input().split())) for _ in range(5)]
num = []
for _ in range(5):
    num += list(map(int, input().split()))
def check():
    cnt = 0
    for r in bingo: # 가로 확인
        if r.count(0) == 5:
            cnt += 1
    for x in range(5): # 세로 확인
        col = 0
        for y in range(5):
            if bingo[y][x] == 0:
                col += 1
        if col == 5:
            cnt += 1
    d1 = 0 # 왼쪽 위 대각선
    for a in range(5):
        if bingo[a][a] == 0:
            d1 += 1
    if d1 == 5:
        cnt += 1
    d2 = 0 # 오른쪽 위 대각선
    for c in range(5):
        if bingo[c][4-c] == 0:
            d2 += 1
    if d2 == 5:
        cnt += 1
    return cnt

answer = 0
for i in range(25):
    for j in range(5):
        for k in range(5):
            if num[i] == bingo[j][k]:
                bingo[j][k] = 0
                answer += 1
    if answer >= 12:
        result = check()
        if result >= 3:
            print(i+1) # 15
            break
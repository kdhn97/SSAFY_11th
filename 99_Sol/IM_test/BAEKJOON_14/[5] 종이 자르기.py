width, length = map(int, input().split()) # width: 10, length: 8
N = int(input()) # 3
dir = [list(map(int, input().split())) for _ in range(N)]
# 가로/세로의 처음 점, 끝 점, 잘린 점들을 담을 배열
W = [0, width]
L = [0, length]

for i in range(N):
    if dir[i][0] == 1: # 세로로 잘린 것들은 가로의 잘린 점들을 담을 배열에 담는다.
        W.append(dir[i][1])
    else: # 반대로 가로로 잘린 것들은 세로 배열에 담는다.
        L.append(dir[i][1])

# 처음 점, 잘린 점들, 끝점 순서로 오도록 오름차순으로 정렬한다.
W.sort()
L.sort()

# 점들 간의 간격을 구해서 가장 큰 값끼리 곱한다.
max_W = max([W[i+1] - W[i] for i in range(len(W)-1)])
max_L = max([L[j+1] - L[j] for j in range(len(L)-1)])
print(max_W * max_L) # 30
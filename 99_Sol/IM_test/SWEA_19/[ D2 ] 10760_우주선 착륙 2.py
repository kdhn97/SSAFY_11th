T = int(input())
for test_case in range(1, T+1): # test_case: 1
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    landing = [] # [[0, 0], [0, 1], ..., [2, 3], [2, 4]]
    picture = [] # [2, 3, 1, 8, 9, 7, 6, 2, 2, 6, 5, 7, 3, 8, 7]
    for i in range(N):
        for j in range(M):
            picture.append(arr[i][j]) # 전체 높이
            if 0 <= i < N and 0 <= j < M:
                landing.append([i, j]) # 각 배열 좌표
    result = [] # [[2, 3, 7, 6], ..., [2, 6, 8, 7]]
    for l in range(len(landing)):
        space = [] # 착률 지점의 주변 구역 높이
        result.append(space)
        for k in range(-1, 2):
            for a in range(-1, 2):
                if 0 <= landing[l][0]+k < N and 0 <= landing[l][1]+a < M:
                    space.append(arr[landing[l][0]+k][landing[l][1]+a])
    cnt = 0
    for n in range(N * M): # 전체 배열 범위
        answer = []
        for p in range(len(result[n])):
            if picture[n] > result[n][p]: # 착륙지 높이보다 낮은 지역이라면
                answer.append(result[n][p])
        if len(answer) >= 4: # 사진 찍을 수 있는 곳이 4방향 이상이라면
            cnt += 1
    print(f'#{test_case} {cnt}') # #1 5
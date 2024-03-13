cnt_switch = int(input()) # 스위치 개수: 8
button = list(map(int, input().split())) # 스위치: 0 1 0 1 0 0 0 1
num_stu = int(input()) # 학생 수: 2
stu = [list(map(int, input().split())) for _ in range(num_stu)]

for s in range(num_stu):
    if stu[s][0] == 1: # 남학생이라면 [1, 3]
        for m in range(cnt_switch):
            if (m+1) % stu[s][1] == 0: # stu[s][1]의 배수
                if button[m] == 0:
                    button[m] = 1
                else: # 0이라면
                    button[m] = 0

    if stu[s][0] == 2: # 여학생이라면 [2, 3]
        for w in range(cnt_switch):
            if stu[s][1]-w == 0 or stu[s][1]+w == cnt_switch+1:
                break
						# if 0 <= stu[s][1]-w and stu[s][1]+w < cnt_switch:
						# 위와 같이 작성하면
						# 대칭이 아니더라도 해당 범위만큼 조사해버린다.
            if button[stu[s][1]-w-1] == button[stu[s][1]+w-1]: # 좌우대칭
                if button[stu[s][1]+w-1] == 1:
                    button[stu[s][1]+w-1] = 0
                    button[stu[s][1]-w-1] = 0
                else:
                    button[stu[s][1]+w-1] = 1
                    button[stu[s][1]-w-1] = 1
            else:
                break

# 한 줄에 20개씩 출력하게 만들기
for i in range(0, cnt_switch, 20):
    print(*button[i:i+20])
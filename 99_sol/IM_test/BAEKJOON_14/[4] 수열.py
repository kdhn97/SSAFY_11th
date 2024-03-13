length = int(input()) # 11
num_lst = list(map(int, input().split())) # 1 5 3 6 4 7 1 3 2 9 5

up_arr = [1] * length # 커지는 경우 갯수
down_arr = [1] * length # 작아지는 경우 갯수

for l in range(length-1): # 연속적으로 커지는 경우
    if num_lst[l] <= num_lst[l+1]:
        up_arr[l+1] = up_arr[l] + 1

for l in range(length-1): # 연속적으로 작아지는 경우
    if num_lst[l] >= num_lst[l+1]:
        down_arr[l+1] = down_arr[l] + 1

max_up = max(up_arr) # 커지는 수 최댓값
max_down = max(down_arr) # 작아지는 수 최댓값

if max_up > max_down: # 커지는 수 > 작아지는 수
    print(max_up)
elif max_up < max_down: # 커지는 수 < 작아지는 수
    print(max_down)
else: # 커지는 수 == 작아지는 수
    print(max_up)
num = int(input()) # 100
max_arr = []
for n in range(num+1):
    arr = [num, n] # 첫번째 값과 두번째 값은 정해져있다
    idx = 1
    while True:
        result = arr[idx-1] - arr[idx]
        if result < 0: # 뺀 값이 음수라면
            break
        arr.append(result)
        idx += 1
    if len(max_arr) < len(arr): # 최댓값 구하기
        max_arr = arr
print(len(max_arr)) # 8
print(*max_arr) # 100 62 38 24 14 10 4 6
square = [list(map(int, input().split())) for _ in range(4)]
arr = [[0] * 101 for _ in range(101)] # 평면 면적 크기

for s in square: # [1 2 4 4]
    x_leng = s[2]-s[0] # 직사각형 x의 길이: 3
    y_leng = s[3]-s[1] # 직사각형 y의 길이: 2
    for x in range(x_leng):
        for y in range(y_leng):
            arr[s[0]+x][s[1]+y] = 1 # 직사각형 자리에 1 삽입
one = 0
for i in range(101):
    one += arr[i].count(1) # 숫자 1 들어간 면적 구하기
print(one) # 26
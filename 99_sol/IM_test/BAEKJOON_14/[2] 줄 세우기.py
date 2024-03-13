N = int(input()) # 5
stu = list(map(int, input().split())) # 0 1 1 3 2
arr = []

for i in range(N):
    if not arr:
        arr.insert(0,i+1)
    else:
        arr.insert(stu[i], i+1)
for j in reversed(arr):
    print(j, end=' ') # 4 2 5 3 1

# insert() - List의 원하는 위치에 원하는 값을 추가
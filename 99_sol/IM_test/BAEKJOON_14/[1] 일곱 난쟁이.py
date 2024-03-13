arr = [int(input()) for _ in range(9)]

a = b = 0
total = sum(arr)
for i in range(9):
    for j in range(i+1, 9):
        if total - (arr[i]+arr[j]) == 100:
            a = arr[i]
            b = arr[j]
arr.remove(a)
arr.remove(b)
arr.sort()
for k in arr:
    print(k)
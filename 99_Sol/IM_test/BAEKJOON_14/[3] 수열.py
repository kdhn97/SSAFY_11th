N, K = map(int,input().split()) # 10 2
arr = list(map(int, input().split()))

result = []
result.append(sum(arr[:K]))
for i in range(N-K):
    result.append(result[i] - arr[i] + arr[k+i])
print(max(result)) # 21
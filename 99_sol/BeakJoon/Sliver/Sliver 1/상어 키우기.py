N, K, T = map(int, input().split())
shark = sorted(list(map(int, input().split())), reverse=True)
while K >= 1:
    if shark[0] < T:
        T += sum(shark[:K])
        break
    for i in range(N):
        if shark[i] < T:
            T += shark.pop(i)
            K -= 1
            N -= 1
            break
    else:
        break
print(T)
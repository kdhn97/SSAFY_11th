T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = 0
    sum_arr = []
    for c in range(abs(len(B) - len(A)) + 1):  # B와 A의 차이만큼 이동할 값 : c
        arr = []
        for a in range(len(A)):
            for b in range(len(B)):
                if a == b and len(B) < len(A):  # A의 길이가 더 길다면
                    arr.append(A[a + c] * B[b])  # A 인덱스를 c 만큼 이동
                elif a == b and len(B) > len(A):  # B의 길이가 더 길다면
                    arr.append(A[a] * B[b + c])  # B 인덱스를 c 만큼 이동

sum_arr.append(sum(arr))  # arr 값을 더해서 sum_arr에 담기

for s in sum_arr:  # max 구하기
    if result < s:
        result = s
print(f'#{test_case} {result}')  # #1 30
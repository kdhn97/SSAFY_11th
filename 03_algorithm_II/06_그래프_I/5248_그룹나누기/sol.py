import sys
sys.stdin = open('input.txt')

def make_set(n): # 집합 만들기
    return [_ for _ in range(n)]

def find_set(x): # 대표자 찾기
    if parents[x] == x:
        return x
    return find_set(parents[x])

def union(x, y): # 같은 집합으로 묶기
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

T = int(input())
for test_case in range(1, T+1): # test_case: 1
    N, M = map(int, input().split()) # N: 4, M: 3
    arr = list(map(int, input().split())) # arr: [1, 2, 3, 4, 4, 2]
    # 1 ~ N번까지 사용하기 위해 N+1개 생성
    parents = make_set(N+1) # parents: [0, 1, 2, 3, 4]
    # 신청서 제출된 번호끼리 union(i*2, i*2+1)
    for i in range(M):
        union(arr[i*2], arr[i*2+1])

    temp = set() # 중복 제거
    for j in range(1, N+1):
        temp.add(find_set(j))

    print(f'#{test_case} {len(temp)}')

#1 {1}
#2 {1, 3, 5}
#3 {1, 4}
#4 {1, 2, 4}
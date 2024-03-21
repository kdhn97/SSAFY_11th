import sys
sys.stdin = open('input.txt')
# 서로소(상호배타) 집합 연산
def make_set(n): # 집합을 만드는 함수
    return [_ for _ in range(n)]

def find_set(x): # 대표자를 찾는 함수
    if parents[x] == x: # 부모가 자기 자신이면
        return x        # 대표자
    return find_set(parents[x]) # 경로 압축을 통해 대표자를 찾음

def union(x, y): # 두 원소를 같은 집합으로 묶는 함수
    x = find_set(x) # x의 대표자 찾기
    y = find_set(y) # y의 대표자 찾기
    if x == y: # 이미 같은 집합에 속해있으면 더 이상 할 필요 없음
        return
    if x < y: # 대표자 번호를 기준으로 작은 쪽으로 합침
        parents[y] = x
    else:
        parents[x] = y

T = int(input())
for test_case in range(1, T+1): # test_case: 2
    N, M = map(int, input().split()) # N: 5, M: 2
    arr = list(map(int, input().split())) # arr: [1, 2, 3, 4]
    # 1 ~ N번까지 사용하기 위해 N+1개의 집합 생성
    parents = make_set(N+1) # parents: [0, 1, 2, 3, 4, 5]
    for i in range(M): # 신청서에 있는 번호들을 짝지어서 같은 집합으로 합침
        union(arr[i*2], arr[i*2+1])

    temp = set() # 중복된 집합을 제거하기 위한 set 생성
    for j in range(1, N+1):
        temp.add(find_set(j)) # 각 원소의 대표자를 찾아서 temp에 추가

    # print(temp) #2 {1, 3, 5}
    print(f'#{test_case} {len(temp)}')
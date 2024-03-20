import sys
sys.stdin = open('input.txt')


T = int(input())

def sum_leaf(n):
    p = n // 2 # 부모 노드의 번호
    if n <= N: # 최대 개수 되기 전가지
        print(tree, n)
        if tree[n] == 0: # 만약 그 잎이 비어있으면
            sum_leaf(n*2) # 왼쪽 탐색
            sum_leaf(n*2+1) # 오른쪽 탐색
        else: # 차있어
            while p > 0: # 그럼 이 잎의 조상들은 다 해당 번호가 더해져야함
                tree[p] += tree[n] # 그 값들을 더해준다
                p //= 2 # 부모를 거슬러 올라간다


for test_case in range(1,T+1):
    N, M, L = map(int,input().split()) # N:노드의 개수, M 리프노드의 개수, L은 출력할값
    tree = [0 for _ in range(N + 1)]  # 값을 넣을 트리 입력
    for _ in range(M): # 리프노드의 입력
        idx, value = map(int,input().split()) # 인덱스 번호와 리프 노드 값
        tree[idx] = value
    sum_leaf(1) # 잎 더해줄게
    print(tree)
    print(f'#{test_case} {tree[L]}')
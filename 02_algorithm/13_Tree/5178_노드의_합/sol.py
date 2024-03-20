import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    leaf = [list(map(int, input().split())) for _ in range(M)]

    tree = [0] * (N + 1)  # 0번 노드 없음
    for idx, value in leaf:  # 단말 노드 값 트리에 삽입
        tree[idx] = value
    print(tree)

    while N != L * 2 - 1:    # L의 직계 자식보다 작은 노드들에 대해서 조사 할 필요 없음
        tree[N//2] += tree[N]
        N -= 1
        print(tree)
    print(L)
    print(f'#{tc} {tree[L]}')
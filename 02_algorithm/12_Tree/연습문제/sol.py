import sys
sys.stdin = open('input.txt')


def solution(k):    # 할일이 노드번호를 출력하는 것,
    print(k, end=' ')

def preorder(now):  # 조사 시작 노드번호부터 조사를 시작한다.
    # 노드 번호 0은 없음
    # 따라서, 노드 번호가 0이 아닌 경우만 조사할 수 있어야함
    if now != 0:
        # 전위 순회는, 조사 시작 노드 번호에 대해서 할 일을 수행
        solution(now)   # 현재 노드 번호에 대해 할일 수행
        # 왼쪽 자식 순회
        preorder(tree[now][0])
        # 오른쪽 자식 순회
        preorder(tree[now][1])

def inorder(now):
    if now != 0:
        inorder(tree[now][0])
        solution(now)
        inorder(tree[now][1])

def postorder(now):
    if now != 0:
        postorder(tree[now][0])
        postorder(tree[now][1])
        solution(now)


V = int(input())
edge = list(map(int, input().split()))
print(edge)
E = len(edge)   # 간선 정보 길이
# 인접 리스트
# adj = [[] for _ in range(V+1)]  # 0번 노드는 없다.
# tree[현재 노드 번호][0] -> 현재 노드 번호의 왼쪽 자식 노드 번호
tree = [[0, 0] for _ in range(V + 1)]
print(tree)
for idx in range(E//2):
    # 특정 위치에 값을 할당 하는 것.
    if tree[edge[idx*2]][0] == 0:   # 왼쪽 자식 정보가 아직 없다면
        # 왼쪽 자식에 자식 정보 삽입
        tree[edge[idx*2]][0] = edge[idx*2+1]
    else:
        # 왼쪽 자식이 이미 있다면 오른쪽에 자식 정보 삽입
        tree[edge[idx * 2]][1] = edge[idx * 2 + 1]
print(tree)
preorder(1)
print()
inorder(1)
print()
postorder(1)
# for idx in range(E//2):
#     adj[edge[idx*2]].append(edge[idx*2+1])
# print(adj)

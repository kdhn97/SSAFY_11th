import sys
sys.stdin = open('input.txt')


def inorder(node):
    if node:
        inorder(int(tree[node][2]))
        print(tree[node][1], end='')
        inorder(int(tree[node][3]))

for tc in range(1, 11):
    N = int(input())
    # 노드번호, 값, 왼쪽, 오른쪽자식
    # 자식이 없을 수 있음
    tree = [input().split() for _ in range(N)]

    tree.insert(0, ['0', '0', '0', '0'])
    # print(tree)
    for node in tree:   # 모든 노드 순회
        # print(node, end =' ')
        while len(node) != 4:   # 없는 자식 정보 누락되었다면
            node.append('0')    # 없는 자식정보를 삽입한다.
        # print(node)
    inorder(1)
    print()
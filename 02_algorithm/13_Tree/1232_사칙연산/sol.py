import sys
sys.stdin = open('input.txt')

def cal(left, right, oper):
    # if oper == '+':
    #     return int(left) + int(right)
    # elif...
    return eval(f'{left}{oper}{right}')  # => '1 + 2'

def postorder(node):
    if node:    # 0이 아니라면,
        if data[node][1].isdecimal():   # 피연산자라면
            return data[node][1]        # 피연산자라면
        else:
            left = postorder(int(data[node][2])) # '0' -> if '0' != False:
            right = postorder(int(data[node][3]))
            return cal(left, right, data[node][1])

for tc in range(1, 11):
    N = int(input())
    data = [input().split() for _ in range(N)]
    data.insert(0, 0)   # 0번 노드 안씀
    result = postorder(1)
    print(f'#{tc} {int(result)}')
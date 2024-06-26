import sys
sys.stdin = open('input.txt')


operator = '+-*/'

def cal(postfix):
    stack = []
    for char in postfix:
        if char.isdecimal():
            stack.append(int(char))
        else:
            x = stack.pop()
            y = stack.pop()
            if char == '+':
                stack.append(y + x)
            elif char == '*':
                stack.append(y * x)
    return stack[-1]

for tc in range(1, 11):
    N = int(input())
    arr = input()
    postfix = ''
    stack = []
    for char in arr:
        if char in operator:
            if not stack:
                stack.append(char)
            else:
                if char == '*':
                    while stack and stack[-1] in '*/':
                        postfix += stack.pop()
                elif char == '+':
                    while stack:
                        postfix += stack.pop()
                stack.append(char)
        else:
            postfix += char
    while stack:
        postfix += stack.pop()

    result = cal(postfix)
    print(f'#{tc} {result}')


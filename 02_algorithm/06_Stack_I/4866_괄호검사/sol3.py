import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    data = input()
    stack = []
    result = 1
    open_bracket = '({'
    close_bracket = ')}'
    for char in data:
        if char in open_bracket:
            stack.append(char)
        elif char in close_bracket:
            if stack:
                if char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
            else:
                result = 0
                break
    if stack:
        result = 0
    print(f'#{tc} {result}')
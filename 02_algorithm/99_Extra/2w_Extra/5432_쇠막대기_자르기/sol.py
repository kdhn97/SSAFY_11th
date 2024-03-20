import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = input()
    # 여는 괄호의 개수를 세기 위함
    len_stack = 0
    # 이전 괄호가 무엇이었느냐를 판단
    last_bracket = ''
    result = 0
    for char in arr:
        # 여는 괄호면 개수 추가
        if char == '(':
            len_stack += 1
        else:   # 닫는 괄호면
            # 이전 괄호가 무엇이었냐에 따라 규칙 변동
            if last_bracket == ')':
                # 이전 괄호가 닫는 괄호였다면,
                # 여는 괄호 개수 하나 감소하고
                # 쇠막대기 하나의 길이가 끝났고, 그 만큼 1증가
                len_stack -= 1
                result += 1
            else:
                # 이전 괄호가 여는괄호였다면
                # 그냥 레이저 발사
                # 여는 괄호 개수 한개 줄이고
                # 모든 쇠막대기 수만큼 증가
                len_stack -= 1
                result += len_stack
        last_bracket = char
    print(f'#{tc} {result}')


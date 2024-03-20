import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    inputs = input()

    inputs_brackets = []
    brackets = ['{', '}', '(', ')']

    # 문자열을 순회하며 괄호만 리스트에 담기
    for i in inputs:
        if i in brackets:
            inputs_brackets.append(i)

    # 괄호 리스트를 순회하며 괄호쌍을 발견하면 발견한 괄호쌍을 제외한 리스트를 괄호 리스트에 재할당
    # 괄호쌍이 더 이상 없으면 중지
    finish = False
    while finish == False:
        for j in range(len(inputs_brackets) - 1):
            if inputs_brackets[j : j + 2] == ['(', ')']:
                inputs_brackets = (inputs_brackets[:j] + inputs_brackets[j + 2 :])
                break
            elif inputs_brackets[j : j + 2] == ['{', '}']:
                inputs_brackets = (inputs_brackets[:j] + inputs_brackets[j + 2 :])
                break
        else:
            finish = True

    # 결과 출력
    if inputs_brackets == []:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')
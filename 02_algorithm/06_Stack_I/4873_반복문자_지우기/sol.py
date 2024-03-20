import sys

sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    word = input()
    # print(word)   # ABCCB
    stack = []

    # input값이 str 형태기 때문에 각각 하나씩 들어감
    for i in word:
        # stack이 비어있으면 i를 append
        # if len(stack) == 0:
        if not stack:  # 이렇게도 쓰더라
            stack.append(i)

        # stack의 마지막 원소와 i가 다르면 append
        elif stack[-1] != i:
            stack.append(i)

        # stack의 마지막 원소와 i가 같으면 pop
        elif stack[-1] == i:
            stack.pop()

    print(f'#{test_case} {len(stack)}')
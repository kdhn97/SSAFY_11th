import sys

sys.stdin = open('input.txt')


class Stack:
    # stack을 생성할 때 필요한 값이 있는데,
    # stack의 크기를 지정해야 한다.
    def __init__(self, size):
        self.size = size
        # 자료구조 stack을 list를 활용해서 구현
        self.data = [None] * size  # 값이 없음을 나타내는 None
        self.top = -1  # 초기 값이 없으므로, top의 위치는 -1

    def push(self, item):  # stack에 값 삽입 -> 삽입할 대상 item을 인자로 받는다.

        if self.is_full():
            print('Stack i Full!')
        else:
            # 받아온 item을 내 data에 top 번째 위치에 삽입한다.
            self.top += 1  # top위치 1 증가
            self.data[self.top] = item

    def get(self):  # top번째 있는 요소를 출력할 수 있는 방법
        return self.data[self.top]

    def __str__(self):  # instance print했을 때, stack안의 data를 바로 출력
        return f'{self.data}'

    def pop(self):
        if self.is_empty():
            print('Stack is Empty!')
            raise IndexError
        else:
            # top_value = self.data[self.top] = None
            # self.data[self.top] = None
            self.top -= 1
            # return top_value
            return self.data[self.top + 1]

    def is_empty(self):
        # top이 -1을 가리키고 있다면 stack은 비었다.
        return self.top == -1

    def is_full(self):
        return self.size == self.top + 1


# stack 사이즈 100짜리 생성 후 , 출력
# stack = Stack(100)
# print(stack.size)
# print(stack.data)
# print(stack.top)
# stack.push(10)
# print(stack.data)
# print(stack.top)
# print(stack.get())
# print(stack)
# print(stack.pop())
# print(stack)

T = int(input())

for tc in range(1, T + 1):
    bracket = input()
    stack = Stack(100)
    # 모든 문자열을 조사
    result = True
    for char in bracket:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if not stack.is_empty():
                stack.pop()
            else:
                result = False
                break
    if not stack.is_empty():
        result = False

    print(f'#{tc} {result}')
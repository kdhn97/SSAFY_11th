import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = input()
    result = 0
    cnt = 0
    is_one = False
    for char in data:
        if char == '1':
            if not is_one:
                is_one = True
            cnt += 1
        else:
            if result < cnt:
                result = cnt
            is_one = False
            cnt = 0
    if result < cnt:
        result = cnt
    print(f'#{tc} {result}')


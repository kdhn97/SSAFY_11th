import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    dump = int(input())
    matrix = list(map(int, input().split()))

    matrix.sort()   # 정렬 한다
    while dump:         # 덤프 가능한 동안 반복
        matrix[0] += 1
        matrix[-1] -= 1
        matrix.sort()
        dump -= 1

    print(f'#{tc} {matrix[-1] - matrix[0]}')





import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 도화지
    matrix = [[0] * 10 for _ in range(10)]
    result = 0
    # N번 만큼 반복하며 입력 받는다.
    for _ in range(N):
        # s, e+1 까지의 범위에 color (1 or 2) 입력
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                # 전체 범위에 색칠
                matrix[r][c] += color
                if matrix[r][c] == 3:   # 1 + 2 == 3
                    # 겹친 영역 표기
                    result += 1
    print(f'#{tc} {result}')

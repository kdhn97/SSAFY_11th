import sys
sys.stdin = open('input.txt')
T = int(input())

def enq(n):
    global last
    last += 1       # 마지막 노드 추가
    h[last] = n     # 마지막 노드에 데이터 삽입
    c = last        # 부모 > 자식 비교를 위해
    p = c // 2      # 부모 번호 계산
    while p >= 1 and h[p] > h[c]:   # 부모가 있는데, 더 작으면
        h[p], h[c] = h[c], h[p]     # 교환

for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    N = int(input())
    nodes = list(map(int, input().split()))
    h = [0] * (N+1)
    last = 0

    for i in nodes:
        enq(i)
    # last_node = h[-1]

    result = 0
    l_num = N
    while l_num > 1:
        l_num //= 2
        result += h[l_num]
    # print(h)
    print(result)
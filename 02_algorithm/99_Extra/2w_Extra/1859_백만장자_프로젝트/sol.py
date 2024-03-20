import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    stack = []
    result = 0
    # 내 앞의 수가 크건 작건
    # 팔 수 있는 날은 다음날부터
    # 즉, 뒤에서부터 조사하며,
    # 앞의 값이 나보다 큰 경우면 손해이므로 무시하고, 판매 가능 수익을 앞 날로 변경
    # 한 칸 앞의 값이 나보다 작으면 내 날짜에 파는 것이 이득이므로 판매
    for idx in range(N-1, -1, -1):
        if not stack:
            stack.append(arr[idx])
        else:
            if stack[-1] > arr[idx]:
                result += stack[-1] - arr[idx]
            else:
                stack.append(arr[idx])
    print(f'#{tc} {result}')

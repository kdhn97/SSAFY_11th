T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    card = list(map(str, input().split()))
    ans = []

    if N % 2 == 1:  # 홀수라면 앞 부분이 하나 많게 파티션을 설치합니다.
        partition = N // 2 + 1
    else:
        partition = N // 2

    for i in range(N // 2):  # 번갈아가면서 card를 ans에 추가합니다.
        ans.append(card[i])
        ans.append(card[i + partition])

    if N % 2 == 1:  # 홀수였다면 추가 한 장을 넣으며 셔플덱을 출력합니다.
        print(f'#{tc}', *ans, card[N // 2])
    else:
        print(f'#{tc}', *ans)
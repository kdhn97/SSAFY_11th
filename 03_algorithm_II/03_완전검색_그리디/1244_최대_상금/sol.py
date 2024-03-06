import sys
sys.stdin = open('input.txt')

# 완전 탐색 활용 (가지치기)
def back_track(k):                      # k -> 교환 횟수
    global ans
    val = int(''.join(cards))           # 숫자 카드
    if val in visited[k]:               # 이미 체크 했다면 종료
        return
    visited[k].add(val)                 # 아니라면 해당 카드 조합을 추가

    if k == cnt:                        # 모든 카드를 교환 했다면(주어진 횟수만큼 교환)
        ans = max(ans, val)             # 최대 금액을 갱신
    else:
        # 카드 조합 -> 최댓값 갱신
        for i in range(num_of_cards-1):
            for j in range(i+1, num_of_cards):
                cards[i], cards[j] = cards[j], cards[i]  # 변경하고
                back_track(k+1)                          # 다음 확인
                cards[i], cards[j] = cards[j], cards[i]  # 원복


T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())
    cards, cnt = list(arr[0]), int(arr[1])  # cards: 카드 목록, cnt: 최대 교환 횟수
    num_of_cards = len(cards)               # 카드 숫자(최대 자릿수 6)
    visited = [set() for _ in range(11)]    # 최대 10회 교환 -> 체크한 숫자 조합 파악 -> set을 활용한 중복 제거
    ans = 0
    back_track(0)   # 0번부터 시작
    print(visited)
    print(f'#{tc} {ans}')
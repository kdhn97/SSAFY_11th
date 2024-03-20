import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    data = list(map(int, input().strip()))
    cards = [0] * (max(data)+1)  # 카드 count 배열 초기화

    # 카드 갯수 카운트
    for i in data:   
        cards[i] += 1

    idx = cnt = 0  # 반복문 제어 idx / 정답 카운트 변수 cnt

    # 같은 값이 3개 이상 있을 때
    while idx < len(cards):
        if cards[idx] >= 3:
            cards[idx] -= 3
            cnt += 1  # baby gin 카운트 증가
            continue  # 5555555 와 같은 경우를 위해 continue
        idx += 1

    idx = 1  # run의 경우 검사를 위한 idx 초기화
    while idx < len(cards)-1:  # 끝까지 검사할 경우 인덱스 에러 발생
        if cards[idx - 1] >= 1 and cards[idx + 1] >= 1 and cards[idx] >= 1:
            cards[idx-1] -= 1
            cards[idx] -= 1
            cards[idx+1] -= 1
            cnt += 1
            continue  # 123123 와 같은 경우를 위해 continue
        idx += 1

    print(f'#{tc} 1') if cnt == 2 else print(f'#{tc} 0')

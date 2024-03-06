import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [2, 3, 5, 7, 11]
    count = [0] * len(arr)  # a~e 개수를 세기 위한 리스트

    idx = 0
    while N != 1:  # 1이 될때까지
        for i in range(len(arr)):  # 후보군으로 나누기
            if not N % arr[i]:  # 나누어 떨어진다면
                N //= arr[i]  # N을 나눈 몫으로 변경
                count[i] += 1  # 해당 후보군 사용 횟수 1 증가
                break  # 다시 최소 값부터 조사를 위해 반복문 종료

    # 리스트의 값을 문자열로 변경한 후,
    # 변경된 문자열을 공백으로 나누어 하나의 문자열로 조합하고 출력
    result = ' '.join(map(str, count))
    print(f'#{tc} {result}')

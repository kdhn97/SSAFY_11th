import sys
sys.stdin = open('input.txt')

# 화물운반
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1 <= T <= 50
T = int(input())
# 다음 줄부터 테스트 케이스의 별로
for test_case in range(1, T + 1):
    # 첫 줄에 컨테이너 수 N과 트럭 수 M이 주어지고
    N, M = map(int, input().split())
    # 다음 줄에 N개의 화물이 무게 wi
    wi_arr = list(map(int, input().split()))
    # 다음 줄에 M개 트럭의 적재용량 ti
    ti_arr = list(map(int, input().split()))
    # wi 배열은 내림차순으로 정렬
    wi_arr.sort(reverse=True)
    # ti 배열은 오름차순으로 정렬
    ti_arr.sort()
    # 결과를 담을 result 변수 초기화
    result = 0
    for wi in wi_arr:  # wi 배열을 순회하면서
        if ti_arr and ti_arr[-1] >= wi:  # wi (가장 큰 트럭 >=현재 제일 무거운 화물)
            result += wi  # 싣어보낸 화물은 결과값에 추가
            ti_arr.pop()  # 해당 트럭은 트럭 배열에서 삭제
    # 결과 값을 테케와 함께 출력
    print(f'#{test_case} {result}')

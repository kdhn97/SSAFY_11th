import sys
sys.stdin = open('input.txt')

N, result = list(map(int, input().split()))

cnt = 1
while N != result:
    if result % 2 == 0: # result가 짝수라면
        result = result // 2 # 2 나누기
        cnt += 1
    elif result % 2 == 1: # result가 홀수라면
        result = list(str(result))
        if result[-1] == '1': # result의 마지막이 1이라면
            result.pop() # 1 제거
            cnt += 1
        result = int(''.join(result))
    if result < N: # result가 더 작아진다면
        print(-1) # 불가능 -1
        break
# N 과 result가 같다면
if N == result:
    print(cnt)
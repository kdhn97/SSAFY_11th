def danzo(n): # 단조 증가하는 수를 검사하는 함수입니다.
    while n >9:  # n이 한자리가 될때까지
        a = n%10 # 현재 일의 자리와
        b = n//10 %10 # 십의 자리를 비교합니다.
        if b>a:
            return 0 # 십의 자리가 더 크다면 단조 증가하는 수가 아닙니다.
        n //= 10 # 일의 자리가 더 크다면 n을 한자리 감소시킵니다.
    return 1  # 위 과정을 모두 통과한다면 단조 증가하는 수입니다.

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    Ai = list(map(int,input().split()))
    mx = 0

    for i in range(N-1):
        for j in range(i+1,N):
            num = Ai[i] * Ai[j] # Ai * Aj를 차례대로 num에 저장합니다

            if danzo(num): #num을 검사하고 단조 증가하는 수이면 mx와 비교합니다.
                if num > mx:
                    mx = num

    if mx == 0:
        mx = -1
    print(f'#{tc}', mx)
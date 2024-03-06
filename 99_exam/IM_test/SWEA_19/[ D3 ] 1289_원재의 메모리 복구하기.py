'''
2
0011
100
'''
def func(n):
    global cnt
    for i in range(len(n)):
        if n[i] == '1': # 만약 1이라면
            # 1부터 뒤의 모든 숫자를 변경
            for j in range(i, len(n)):
                if n[j] == '1':
                    n[j] = '0'
                else:
                    n[j] = '1'
            cnt += 1 # 변경할 때마다 cnt 증가
            if '1' in n: # 만약 1이 남았다면
                func(N)
    if '1' not in N: # 만약 1이 없다면
        return cnt


T = int(input())
for test_case in range(1, T + 1):
    N = list(map(str, input()))
    cnt = 0 # 수정 횟수
    func(N)
    print(f'#{test_case} {cnt}')
'''
#1 1
#2 2
'''
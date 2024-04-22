import sys
sys.stdin = open('algo2_sample_in.txt')

'''
r : 1 ~ N-1 번까지의 다리를 사용 여부
acc : 건설 비용
cnt : 다리 개수
'''
def search(r, acc, cnt):
    global result, cnt_result
    if acc > V:     # 누적값이 한번이라도 예산을 초과한 경우,
        return      # 더 이상 조사 할 필요 없음
    elif cnt + (N-r) < cnt_result:
        # 지금까지 사용한 다리 개수 + 남은 다리 개수가
        # 이전에 만든 최대 다리 사용 개수보다 작으면
        # 더 이상 조사 할 필요 없다.
        return
    if r == N:  # 모든 다리 사용 여부 판별 완료
        if acc < V: # 누적값이 총 예산보다 작은 경우에만
            if cnt >= cnt_result:
                if cnt == cnt_result:
                    result = min(result, acc)
                else:
                    result = acc
                cnt_result = cnt
    else:
        # r번째 다리를 썻든 안 썼든, 어쨋든 다음 다리 조사하러갈 예정
        search(r + 1, acc + Ci[r], cnt + 1) # r번째 다리를 사용한 경우
        search(r + 1, acc, cnt) # r번째 다리를 사용하지 않은 경우

T = int(input())

for tc in range(1, T+1):
    N, V = map(int, input().split())
    Ci = list(map(int, input().split()))
    result = 0      # 최소 비용
    cnt_result = 0  # 최대 다리 수
    search(0, 0, 0)
    print(f'#{tc} {cnt_result} {result}')

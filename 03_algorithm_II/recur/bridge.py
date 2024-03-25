'''
< 문제 >
싸피 군도에 예산을 초과하지 않는 범위에서 최대한 많은 다리를 놓으려고
한다. 책정된 예산과 각 섬 사이에 다리를 놓는 비용이 주어질 때, 건설할 수
있는 최대 다리 수와 이때의 건설비용을 출력하는 프로그램을 만들어라. 건설할
수 있는 최대 다리 개수가 같은 경우, 건설 비용이 적은 쪽을 택한다.
'''

'''
< 입력값 >
3
3 35
11 10 19
4 826
559 281 278 27
5 572
88 255 570 839 39
'''

# r : 1 ~ N-1 번까지의 다리를 사용 여부, acc : 건설 비용, cnt : 다리 개수
def search(r, acc, cnt):
    global result, cnt_result
    if acc > V: # 누적값이 한번이라도 예산을 초과한 경우,
        return  # 더 이상 조사할 필요 없음
    elif cnt + (N-r) < cnt_result:
        # 지금까지 사용한 다리 개수 + 남은 다리 개수가
        # 이전에 만든 최대 다리 사용 개수보다 작으면
        # 더 이상 조사할 필요 없다.
        return
    if r == N:      # 모든 다리 사용 여부 판별 완료
        if acc < V: # 누적값이 총 예산보다 작은 경우에만
            if cnt >= cnt_result:
                if cnt == cnt_result:
                    result = min(result, acc)
                else:
                    result = acc
                cnt_result = cnt
    else:
        # r번째 다리를 썻든 안썻든 다음 다리 조사하러 갈 예정
        search(r+1, acc+Ci[r], cnt+1) # 다리를 사용한 경우
        search(r+1, acc, cnt) # 다리를 사용하지 않은 경우

T = int(input())
for test_case in range(1, T+1):
    N, V = map(int, input().split())
    Ci = list(map(int, input().split()))
    result = 0     # 최소 비용
    cnt_result = 0 # 최대 다리 수
    search(0, 0, 0)
    print(f'#{test_case} {cnt_result} {result}')

'''
< 출력값 >
#1 2 21
#2 3 586
#3 3 382
'''
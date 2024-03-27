import sys
sys.stdin = open('input.txt')

N = int(input())
answer = [] # [40, 80, 70, 50, 10, 20, 100, 70, 30]
for i in range(N):
    score = list(map(int, input().split())) # [40, 80, 70]
    sorted_score = sorted(score, reverse=True) # [80, 70, 40]
    ranks = [sorted_score.index(s)+1 for s in score] # [3, 1, 2]
    print(*ranks) # 각 점수 순위

    answer += score

sum_score = [] # [190] [160] [120]
for i in range(N):
    result = [] # [40, 50, 100] [80, 10, 70] [70, 20, 30]
    for j in range(i, len(answer), N):
        result.append(answer[j])
    sum_score.append(sum(result))
sorted_sum_score = sorted(sum_score, reverse=True)
sum_ranks = [sorted_sum_score.index(s)+1 for s in sum_score]
print(*sum_ranks) # 최종합계 점수 순위
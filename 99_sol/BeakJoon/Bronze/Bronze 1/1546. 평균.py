N = int(input())
score = list(map(int, input().split()))

new_sum = 0
for s in score:
    max_score = max(score)
    new_score = s / max_score * 100
    new_sum += new_score
print(new_sum/N)
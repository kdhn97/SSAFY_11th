import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    score = [list(map(int, input().split())) for _ in range(N)]

    sorted_score = sorted(score, reverse=True)
    ranks = [sorted_score.index(score[s])+1 for s in range(len(score))]
    print(ranks)


'''
3 1 2
1 3 2
1 2 3
1 2 3

1 1 3
2 3 1
3 1 1
1 1 1
'''
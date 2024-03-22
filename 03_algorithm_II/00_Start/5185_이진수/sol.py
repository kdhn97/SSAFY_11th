import sys
sys.stdin = open('input.txt')

for test_case in range(1,int(input())+1):
    N, S = input().split() # N: 4, S: 47FE
    answer = ''
    for i in range(int(N)):
        answer += bin(int(S[i],16))[2:].zfill(4)
    print(f"#{test_case} {answer}") # #1 0100011111111110
import sys
sys.stdin = open('input.txt')

# 자연수 number를 입력 받아, 아래와 같이 높이가 number인 삼각형을 출력하시오.
# 입력 예시 7
# 출력 예시
'''
*
**
***
****
*****
******
*******
'''
N = int(input())
# range는 0부터 N-1 까지지만, 별은 1개부터 N개까지 필요하므로...
for i in range(1, N+1):
    for j in range(i):
        print('*', end='')
    print()

for i in range(1, N+1):
    print('*'*i)
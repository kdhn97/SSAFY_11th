import sys
sys.stdin = open('input.txt')

# 자연수 주어짐
N = int(input())

# 전부 더해야함 -> 그 값을 출력해함
result = 0
# 전부? 순회해야징
for num in range(1, N+1):
    result += num
print(result)
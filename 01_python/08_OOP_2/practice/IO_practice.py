# # 파이썬에서 데이터를 입력 받는 함수.
# num1 = int(input()) # 입력받은 값을 `문자열`로 반환
# num2 = int(input())
# # num2 = int(num2)
# print(num1)
# print(type(num1))
# # print(repr(num1))
# print(num1 + num2)

# # 2번 입력 받는다 -> for 사용해서 2번 똑같은코드
# # 근데 2번 입력 받은 값을.. 더해서 출력해야하는데..
# result = 0
# for i in range(2):
#     num = int(input())
#     result = result + num
#     # print(num, result)
# print(result)

import sys
# txt 파일의 각 줄을의 내용을
# input 함수가 실행 될 때마다, 넣어준다.
sys.stdin = open('input.txt')

N = int(input())
# N번 만큼 입력이 주어진다 했으니, N번만큼 반복해서 input
# result = []
# for i in range(N):
#     # str.split() -> 공백을 기준으로 쪼개서 리스트에 다음
#     arr = input().split()
#     # 모든 요소 순회해서 정수로 바꿔서 다시 리스트만들기
#     digit_list = []
#     for num in arr:
#         digit_list.append(int(num))
#     # print(digit_list)
#     result.append(digit_list)
# print(result)

# result = []
# for i in range(N):
#     arr = list(map(int, input().split()))
#     result.append(arr)
# print(result)

result = [list(map(int, input().split())) for _ in range(N)]
print(result)

# arr1 = input()
# arr2 = input()
# arr3 = input()
print(N)
# print(arr1)
# print(arr2)
# print(arr3)
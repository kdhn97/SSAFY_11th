        #   0    1    2    3
my_list = ['가','나','다','라']

# 4번 인덱스는 없으니까 오류가 날까?
# 슬라이싱으로 범위를 벗어난 경우,
# 예외 처리가 되지 않아서 예상하지 못한 상황 발생 할 수 있다.
print(my_list[2:4]) # ['다','라']
# 예상과 달리 출력 결과는 ['다','라']이다.
print(my_list[4]) # IndexError: list index out of range
print(my_list[2:3]) # ['다']
my_set = {'가', '나', (0, 0)}
my_dict = {
        '가': 1, 
        (0, 0): '튜플도 키값으로 사용가능'
    }

for item in my_set:
    # set 순회로 얻은 요소를 key로 하는 value출력
    # get method -> 함수,
        # 하는 일 : 딕셔너리에서 인지로 넘겨받은 값을 key로 하는 value를 return
        # 근데 key가 없으면 None을 return
    print(my_dict.get(item))
    # 대괄호 접근법으로 key입력시, 해당 키가 없으면 keyError 발생

var = {(1,2,3,'A') : '변수로도 키 설정 가능'}
my_dict.update(var)
print(my_dict)
number_of_people = 0
print('현재 가입 된 유저 수 : ',number_of_people)

def increase_user():
    number_of_people = 0
    number_of_people += 1
    print('현재 가입 된 유저 수 : ',number_of_people)

def create_user(name='홍길동',age=30,address='서울'):
    print(f'{name}님 환영합니다!')
    print({'name':name, 'age':age, 'address':address})
    return name, age, address
    
create_user(name='홍길동',age=30,address='서울')
increase_user()
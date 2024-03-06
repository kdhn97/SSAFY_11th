############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def check_email(user):
    email = user['email']
    # @ 문자열이 email에 포함되어 있냐 마냐
    # 가정: 없다 -> False를 반환한다.
    result = False
    for char in email:
        # 만약 있다면
        if char == '@':
            # 가정이 틀렸으므로 값 변경
            result = True
    return result
    
def check_email(user):
    if '@' in user['email']:
        return True
    else:
        return False

def check_email(user):
    return '@' in user['email']
    



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'user_id': 'leessafy24',
    'password': 'q1w2e3r4',
    'password_confirm': 'q1w2e3r4',
    'email': 'chibbo24@mail.com',
}
print(check_email(user_data1))  # True

user_data2 = {
    'user_id': 'edu',
    'password': 'q1w2e3r4',
    'password_confirm': 'asdf123',
    'email': 'mail24.mail.com',
}
print(check_email(user_data2))  # False
#####################################################

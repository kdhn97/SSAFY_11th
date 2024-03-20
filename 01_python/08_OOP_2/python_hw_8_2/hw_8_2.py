# 아래 함수를 수정하시오.
def check_number():
    # 사용자로부터 값을 입력 받을 예정
    try:
        num = int(input())
        if num > 0:
            print('양수입니다.')
        elif num == 0:
            print('0입니다.')
        else:
            print('음수입니다.')
    except ValueError:
        print('잘못된 입력입니다.')
        print('정수로 나타낼 수 있는 값을 입력해 주세요. ex) 1')
        check_number()

check_number()

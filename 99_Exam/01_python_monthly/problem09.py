############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 재귀함수를 이용하여 구현합니다.
def dec_to_bin(n):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    if n <= 1:
        return str(n)
    else:
        return dec_to_bin(n // 2) + dec_to_bin(n % 2)

def dec_to_bin(n):
    # 주어진 n을 이로 나눠서 몫이 1이 될 때까지 반복
    if n <= 1:
        return str(n)
    else:
        # 다음번 n이 2로 나눈 몫
        new_n = n // 2
        return dec_to_bin(new_n) + dec_to_bin(n % 2)



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(dec_to_bin(55))   # 110111
print(dec_to_bin(15))   # 1111
#####################################################

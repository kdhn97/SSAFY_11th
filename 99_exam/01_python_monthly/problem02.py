############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 len, sum 함수를 사용하지 않습니다.
def average_cost(cost_list):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    result = 0
    all_cost = 0
    length = 0
    for cost in cost_list:
        all_cost += cost
        length += 1
    return all_cost / length

def average_cost(cost_list):
    # 반환 최종결과
    result = 0 # 나 정수 담을거야
    # 평균을 구한다 -> 전체 합 / 전체 길이
    # return sum(cost_list) / len(cost_list)
    all_cost = 0
    length = 0
    # cost_list가 가진 모든 요소 순회해서 출력
    for cost in cost_list:
        # print(cost)
        # 임시 변수 temp
        # 전체 합을 담을 변수에 현재 있는 값 + cost
        temp = all_cost + cost
        # print(temp, 'temp 변수에 할당된 값')
        all_cost = temp
        # length 변수가 가진 값에 1증가한 값을
        # 다시 length에 재 할당
        length = length + 1
        # print(length)
    # print(all_cost, length, all_cost / length)
    return all_cost / length


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(average_cost([25, 40, 50, 55]))  # 42.5
print(average_cost([60, 70, 90, 80, 100, 35])) # 72.5
#####################################################

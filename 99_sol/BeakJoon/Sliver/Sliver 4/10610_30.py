n = '80875542' # 사용자로부터 입력값을 받음

if "0" not in n: # 입력값에 0이 없으면
    print(-1) # -1을 출력

else:  # 입력값에 0이 포함되어 있으면
    num_sum = 0 # num_sum: 39
    for i in range(len(n)):  # 입력값의 각 자리 숫자를 반복
        num_sum += int(n[i]) # 각 자리 숫자를 정수로 변환하여 합에 더함

    if num_sum % 3 != 0: # 숫자의 합이 3으로 나누어 떨어지지 않으면
        print(-1) # -1을 출력
    
    else: # 숫자의 합이 3으로 나누어 떨어지면
        sorted_num = sorted(n, reverse=True) # 입력값을 내림차순으로 정렬
        # sorted_num: ['8','8','7','5','5','4','2','0']
        answer = "".join(sorted_num) # 정렬된 숫자들을 문자열로 합침
        print(answer) # 결과 출력
round = int(input())
for r in range(round):                    # 2명이 게임하므로 1라운드당 2배씩
    N_A = list(map(int, input().split())) # 첫번째 사람 A의 카드 추출
    N_B = list(map(int, input().split())) # 두번째 사람 B의 카드 추출

    card_list_A = []    # A의 카드 번호 담을 리스트 생성
    card_list_B = []    # B의 카드 번호 담을 리스트 생성

    card_cnt_A = N_A[0] # 모든 N1의 첫번째 값(카드 갯수) 추출
    card_cnt_B = N_B[0] # 모든 N2의 첫번째 값(카드 갯수) 추출

    for cnt in range(1,card_cnt_A+1):
        card_list_A.append(N_A[cnt]) # N_A의 카드가 리스트에 담김

    for cnt in range(1,card_cnt_B+1):
        card_list_B.append(N_B[cnt]) # N_B의 카드가 리스트에 담김
				# A카드 숫자 갯수 추출
        A1 = card_list_A.count(1)
        A2 = card_list_A.count(2)
        A3 = card_list_A.count(3)
        A4 = card_list_A.count(4)
				# B카드 숫자 갯수 추출
        B1 = card_list_B.count(1)
        B2 = card_list_B.count(2)
        B3 = card_list_B.count(3)
        B4 = card_list_B.count(4)

    if A4!=B4: # A가 이긴 경우
        if A4 > B4:
            print('A')
    elif A4==B4 and A3!=B3:
        if A3 > B3:
            print('A')
    elif A4==B4 and A3==B3 and A2!=B2:
        if A2 > B2:
            print('A')
    elif A4==B4 and A3==B3 and A2==B2 and A1!=B1:
        if A1 > B1:
            print('A')

    if  B4!=A4: # B가 이긴 경우
        if B4 > A4:
            print('B')
    elif B4==A4 and B3!=A3:
        if B3 > A3:
            print('B')
    elif B4==A4 and B3==A3 and B2!=A2:
        if B2 > A2:
            print('B')
    elif B4==A4 and B3==A3 and B2==A2 and B1!=A1:
        if B1 > A1:
            print('B')

    else: # A와 B가 비긴 경우
        print('D')
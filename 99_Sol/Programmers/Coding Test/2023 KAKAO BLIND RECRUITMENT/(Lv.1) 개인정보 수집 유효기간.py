today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]

def solution(today, terms, privacies):
    today_spt = today.split('.')
    day = ((int(today_spt[0])-2000)*12*28) + (int(today_spt[1])*28) + int(today_spt[2])
    # today의 총 일수 : (2022년-2000)*12*28 + 5월*28 + 19일 = 7511

    # 개인정보 유효기간 * 28 = 총 유효기간 일수
    terms_spt = [] # [['A', 168], ['B', 336], ['C', 84]]
    for i in range(len(terms)):
        t = terms[i].split(' ')
        terms_spt.append([t[0], int(t[1])*28])

    priva_spt = [] # [['2021','05','02','A'], ['2021','07','01','B'], ['2022','02','19','C'], ['2022','02','20','C']]
    for i in range(len(privacies)):
        p = privacies[i].split('.') # privacies를 '.' 기준으로 split
        priva_spt.append(p)
    for j in range(len(priva_spt)):
        p = priva_spt[j][2].split(' ') # priva_spt의 날짜와 약관종류 분리
        priva_spt[j].pop()
        priva_spt[j].extend(p)

    priva_arr = [] # [[7198, 'A'], [7253, 'B'], [7467, 'C'], [7468, 'C']]
    for i in range(len(priva_spt)):
        priva_sum = ((int(priva_spt[i][0])-2000)*12*28) + (int(priva_spt[i][1])*28) + (int(priva_spt[i][2]))
        priva_arr.append([priva_sum, priva_spt[i][3]]) # priva_arr에 (priva_spt의 년월일을 일수로 계산 + 약관 종류) 넣기

    result = [] # 파기해야 할 개인정보
    for i in range(len(terms_spt)):
        for j in range(len(priva_arr)):
            if terms_spt[i][0] == priva_arr[j][1]:
                if day >= terms_spt[i][1] + priva_arr[j][0]: # (유효기간 + 수집일자)가 오늘 날짜보다 작다면 파기해야 하므로
                    result.append(j+1) # 0부터 시작하므로 +1 해준다.
    print(sorted(result))

solution(today,terms,privacies)
def capitalize_words(word):
     # 최종 결과물 : title화 된 문자열
    result = ''
     # word가 가진 요소 모두 순회
     # 조사 조건
        # 첫 번째 글자거나, 글자가 공백 다음에 나타나면
        # 첫 번째 글자임을 알 수 있는 방법
        # index가 0이면 첫 번째 글자임
        # index와 요소 자체 둘다 필요한 상황
     # enumerate와 range로 순회하는 차이는 뭘까?
     # range의 원목적 : 범위를 상정 -> 범위를 내가 자유롭게 작성가능
        # range로 범위를 산정한 경우 : index만 나오므로
        # 요소를 보려면 word[index] 형식으로 작성해야한다
     # enumerate의 목적 : 순회 가능 요소의 각 요소와 index를 함께 반환

    #  for index, char in enumerate(word):
    #       print(index, char)
    result = ''
    temp = ''
    for index in range(len(word)):
        # 현재 순회중인 index번호가 0이거나 이전 글자가 ''이라면
        # 내 위치 : index -> 내 앞 번째 index - 1
            # 단 주의할 것, index가 0일 때, index-1을 조사하게 되면
            # 범위가 이상해질 수 있다
            # 따라서 조건 잘 작성해야 한다.
        if index == 0 or temp == '':
            # index번째 요소를 대문자로 바꿔서
            result += word[index].upper()
        else:
            result += word[index]
        # 위에서 조사할 때는 영향 안 미치도록
        # 각종 조사가 모두 끝나고 다음 순번 넘어가기 전에
        temp = word[index]
    return result

result = capitalize_words("hello, world!")
print(result)
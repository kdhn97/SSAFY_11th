# 아래 함수를 수정하시오.
def count_character(word, char):
    # char -> 단어 하나 char
    # 문자열 : string
    return word.count(char)

def count_character(word, char):
    # 최종 결과물
    result = 0 # 해당하는 알파벳이 나올때마다 1씩 증가
    # 전체 순회
    for text in word:
        # print(text)
        # 순회해서 얻은 text 변수에 든 값이
        # char 매개변수에 들어있는 값과 일치 하다면
        if text == char:
            # result에 담긴 값이 1씩 증가해야한다.
            # tmp = result + 1
            # result = tmp
            # result = result + 1
            # 복합 연산자 +=
            result += 1
    # 전체 순회를 완료 했다 -> 모든 상황에 대한 조사가 끝났다.
    return result

result = count_character("Hello, World!", "o")
print(result)  # 2

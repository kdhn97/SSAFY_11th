import sys
sys.stdin = open("input.txt")

# 숫자와 해당 단어 매핑
word_to_number = {
    "ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4,
    "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9
}

# 역 매핑
number_to_word = {v: k for k, v in word_to_number.items()}

# 테스트 케이스 수 입력
test_cases = int(input())

for case in range(1, test_cases + 1):
    # 케이스 번호와 길이 입력
    input_line = input().split()
    case_number = input_line[0]
    length = int(input_line[1])

    # 문자열 입력 및 분할
    string_input = input().split()

    # 각 단어를 숫자로 변환하여 정렬
    numbers = [word_to_number[word] for word in string_input]
    numbers.sort()

    # 숫자를 단어로 다시 변환하여 출력
    sorted_words = [number_to_word[num] for num in numbers]
    sorted_string = ' '.join(sorted_words)

    # 결과 출력
    print(f"{case_number} {sorted_string}")
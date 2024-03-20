import sys
sys.stdin = open('input.txt')

# 문자열을 뒤에서부터 더해나간다.
def is_palind(word):
    tmp = ''
    for i in range(len(word)-1, -1, -1):
        tmp += word[i]
    # 새로 만든 뒤집힌 문자와 원본이 같다면 회문
    return tmp == word

for tc in range(1, 11):
    N = int(input())
    data = [list(map(str, input())) for _ in range(8)]

    result = 0

    # 8열 or 8행을 모두 순회
    for i in range(8):
        # 그중, 회문의 길이 N을 뺀 길이만큼 순회
        for j in range(8-N+1):
            tmp_word_1 = ''     # 가로 회문
            tmp_word_2 = ''     # 세로 회문
            for k in range(N):
                tmp_word_1 += data[i][j+k]      # 행 우선 순회
                tmp_word_2 += data[j+k][i]      # 열 우선 순회
            # 두 문자열에 대해 회문인지 판별
            if is_palind(tmp_word_1):
                result += 1
            if is_palind(tmp_word_2):
                result += 1

    print(f'#{tc} {result}')

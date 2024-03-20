import sys
sys.stdin = open('input.txt')

# 슬라이싱으로 회문 판별하는 함수
def slicing(word):
    return word[::-1]

# for 문으로 회문 판별하는 함수
def index_for(word):
    result = ''
    for i in range(len(word)-1, -1, -1):
        result += word[i]
    return result

# while문으로 회문 판별하는 함수
def index_while(word):
    result = ''
    N = len(word)
    while N:
        N -= 1
        result += word[N]

    return result

# 메서드와 빌트인펑션으로 회문 판별하는 함수
def inefficient_function(word):
    return ''.join(list(reversed(word)))

T = int(input())

for tc in range(1, T+1):
    word = input()
    result = slicing(word)
    result = index_for(word)
    result = index_while(word)
    result = inefficient_function(word)

    print(f'#{tc}', end=' ')
    if word == result:
        print(1)
    else:
        print(0)
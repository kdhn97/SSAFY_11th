import sys
sys.stdin = open('input.txt')

T = int(input()) # 테스트 케이스: 1
for test_case in range(1, T + 1):
    short_s = str(input()) # XYPV
    long_s = str(input()) # EOGGXYPVSY

    lst = [] # 같은 글자의 갯수를 담을 리스트
    for ss in range(len(short_s)):
        for ls in range(len(long_s)):
            if short_s[ss] == long_s[ls]: # 각 문자열의 글자가 일치한다면
                cnt = long_s.count(long_s[ls]) # 같은 글자의 갯수 추출
                lst.append(cnt) # 추출 값 리스트에 담기
    print(f'#{test_case} {max(lst)}')
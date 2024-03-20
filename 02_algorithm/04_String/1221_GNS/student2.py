import sys
sys.stdin = open('input.txt')

T = int(input()) # T: 10
for test_case in range(1, T + 1): # test_case: 1
    N, M = list(map(str, input().split())) # N: #1, M: 7041
    str_num = list(map(str, input().split())) # SVN FOR ZRO...
    # ZRO부터 NIN까지의 모든 리스트 생성
    result_ZRO = []
    result_ONE = []
    result_TWO = []
    result_THR = []
    result_FOR = []
    result_FIV = []
    result_SIX = []
    result_SVN = []
    result_EGT = []
    result_NIN = []
    # 해당 글자에 속한 리스트에 담기
    for m in range(int(M)):
        if str_num[m] == 'ZRO':
            result_ZRO.append('ZRO')
        if str_num[m] == 'ONE':
            result_ONE.append('ONE')
        if str_num[m] == 'TWO':
            result_TWO.append('TWO')
        if str_num[m] == 'THR':
            result_THR.append('THR')
        if str_num[m] == 'FOR':
            result_FOR.append('FOR')
        if str_num[m] == 'FIV':
            result_FIV.append('FIV')
        if str_num[m] == 'SIX':
            result_SIX.append('SIX')
        if str_num[m] == 'SVN':
            result_SVN.append('SVN')
        if str_num[m] == 'EGT':
            result_EGT.append('EGT')
        if str_num[m] == 'NIN':
            result_NIN.append('NIN')
    # ZRO부터 NIN까지 순서대로 이어붙이기
    result = ' '.join(map(str, result_ZRO+result_ONE+result_TWO+
                          result_THR+result_FOR+result_FIV+result_SIX+
                          result_SVN+result_EGT+result_NIN))
    print(N)
    print(result)
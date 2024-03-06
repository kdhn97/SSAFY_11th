import sys
sys.stdin = open('input.txt')

def boyer_moore(patten, target):
    lps = {patten[idx]: len(patten)-1-idx for idx in range(len(patten))} # 스킵 가능한 범위 기록
    patten_index = len(patten)
    target_index = 0

    while target_index <= len(target) - patten_index:
        for p_idx in range(patten_index-1, -1, -1):
            if target[target_index + p_idx] != patten[p_idx]:
                target_index += lps.get(target[target_index + p_idx])
                break # 틀렸으니까 p_idx 다시 len(patten)-1 되도록 조사종료
        else:
            return True
    return False
T = int(input()) # T: 3
for test_case in range(1, T + 1): # test_case: 1
    str1 = input()
    str2 = input()
    result = 0 # 없다면 0
    boyer_moore(str1, str2)
    if str1 in str2:
        result = 1 # 있다면 1
    print(f'#{test_case} {result}')

# def KMP(patten, target):
#     def make_lps():
#         # 내 앞에 나와 동일한 패턴이 몇번 나왔는지 세어주는 리스트
#         lps = [0] * len(patten)
#         for idx in range(1, len(patten)): # 0번 인덱스는 앞에 중복되는 값 없음
#             if patten[lps[idx-1]] == patten[idx]:
#                 lps[idx] = idx[idx-1] + 1
#         lps.insert(0, -1)
#         return lps
#     lps = make_lps()
#
#     # 둘 다 첫 조사 시작지점 0번에서 시작
#     patten_index = 0
#     target_index = 0
#     # 현재 조사위치가 조사대상의 범위를 벗어나기 전까지
#     while target_index < len(target):
#         print(lps[patten_index])
#         print(target_index, target[target_index], patten_index, patten[patten_index])
#         if patten[patten_index] != target[target_index]:
#             patten_index = -1
#         target_index += 1
#         patten_index += 1
#         # 패턴의 끝까지 index가 증가했다
#         # -> target과 patten이 일치하지 않는 부분 없이
#         # 패턴의 끝까지 조사했다
#         if patten_index == len(patten):
#             return True
#     return False

# def brute_force(patten, target):
#     # 둘 다 첫 조사 시작지점 0번에서 시작
#     patten_index = 0
#     target_index = 0
#     # 현재 조사위치가 조사대상의 범위를 벗어나기 전까지
#     while target_index < len(target):
#         # 일치하지 않으면
#         if patten[patten_index] != target[target_index]:
#             patten_index = -1
#         # 일치하면
#         target_index += 1
#         patten_index += 1
#         # 패턴의 끝까지 index가 증가했다
#         # -> target과 patten이 일치하지 않는 부분 없이
#         # 패턴의 끝까지 조사했다
#         if patten_index == len(patten):
#             return True
#     return False


#     short_str = str(input()) # short_str: 'XYPV'
#     long_str = str(input()) # long_str: 'EOGGXYPVSY'
#
#     result = [] # long_str의 값을 len(short_str)만큼 부분추출
#
#     for i in range(len(long_str)):
#         if i <= len(long_str) - len(short_str): # 추출 범위 지정
#             for s in long_str:
#                 result = long_str[i:len(short_str)+i]
#
#         if result in short_str: # 만약 일치한다면
#             print(f'#{test_case} 1')
#             break # 하나라도 찾는다면 break
#
#     if result not in short_str: # 만약 일치 않는다면
#         print(f'#{test_case} 0')
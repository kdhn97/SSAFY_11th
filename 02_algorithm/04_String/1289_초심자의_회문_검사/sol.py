import sys
sys.stdin = open('input.txt')

T = int(input()) # T: 3
for test_case in range(1, T + 1): # test_case: 1
    arr = str(input()) # arr: level

    # 방법 1
    # if arr == arr[::-1]: # arr과 arr을 반대로 뒤집은 문자는 같은가?
    #     print(f'#{test_case} 1') # 같다면
    # else:
    #     print(f'#{test_case} 0') # 다르다면

    # 방법 2
    for i in range(len(arr)): # arr의 범위 인덱스: i

        if arr[i-1] == arr[-i]: # arr 문자와 대칭이 되는 문자가 같다면
            print(f'#{test_case} 1')
            break
        else: # 다르다면
            print(f'#{test_case} 0')
            break
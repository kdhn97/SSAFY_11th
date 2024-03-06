import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(8)]

    # 가로 세기
    # cnt_row = 0
    # lst1 = []
    # lst2 = []
    # for i in range(8):
    #     for j in range(8-N+1):
    #         for k in range(N):
    #             lst1.append(arr[i][j+k])
    #             lst2.append(arr[i][-j+k])
    #     for a in range(len(lst1)):
    #         a_list = ''.join(lst1[a:a+N])
    #     for b in range(len(lst2)):
    #         b_list = ''.join(lst2[b:b+N])
    #     if a_list == b_list:
    #         cnt_row += 1

    # # 세로 세기
    # cnt_col = 0
    # lst3 = []
    # lst4 = []
    # for j in range(8 - N + 1):
    #     for i in range(8):
    #         for k in range(N):
    #             lst3.append(arr[j+k][i])
    #             lst4.append(arr[j+k][-i])
    #     for c in range(len(lst3)):
    #         c_list = ''.join(lst3[c+N:c])
    #     for d in range(len(lst4)):
    #         d_list = ''.join(lst4[d+N:d])
    #     if c_list == d_list:
    #         cnt_col += 1

    # cnt = cnt_row + cnt_col
    # print(f'#{test_case} {cnt}')
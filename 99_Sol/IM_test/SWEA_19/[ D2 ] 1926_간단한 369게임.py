N = int(input()) # 10
for n in range(1, N+1):
    # print(list(str(n)))
    lst = list(str(n))

    cnt_369 = []
    cnt_369.append(lst.count('3') + lst.count('6') + lst.count('9'))

    for g in range(len(cnt_369)):
        if cnt_369[g] == 0:
            print(''.join(lst), end=' ')
        elif cnt_369[g] == 1:
            print('-', end=' ')
        elif cnt_369[g] >= 2:
            print('-' * cnt_369[g], end=' ')
'''
1 2 - 4 5 - 7 8 - 10
'''
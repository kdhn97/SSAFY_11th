one = 3
two = 5
print(one or two)
if one and two:
    print('and 연산 통과')
else:
    print('and 연산 통과 못함')

print(0 == False)
print(-1 == False)
print('' == False)
print('' == True)

if '':
    print('빈문자열?')
else:
    print('아무일도...')

three = ''
four = '4'
print(three and four)
if three and four:
    print('3과 4')
else:
    print('실패')

if one % 2:
    print('홀수')
if one % 2 == 1:
    print('홀수')
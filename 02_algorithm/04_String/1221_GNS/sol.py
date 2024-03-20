import sys
sys.stdin = open('input.txt')

text_to_decimal = {
    "ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4,
    "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9
}

T = int(input())

for tc in range(1, T+1):
    tc, N = map(lambda x: int(x) if x.isdecimal() else x, input().split())
    data = sorted(input().split(), key=lambda x: text_to_decimal[x])
    print(f'{tc}', *data)
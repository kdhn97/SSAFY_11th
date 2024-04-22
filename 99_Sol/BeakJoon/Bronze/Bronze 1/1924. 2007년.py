import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
day = 0

if N == 1:
    day = M
if N == 2:
    day = 31+M
if N == 3:
    day = 59+M
if N == 4:
    day = 90+M
if N == 5:
    day = 120+M
if N == 6:
    day = 151+M
if N == 7:
    day = 181+M
if N == 8:
    day = 212+M
if N == 9:
    day = 243+M
if N == 10:
    day = 273+M
if N == 11:
    day = 304+M
if N == 12:
    day = 334+M

week = day % 7

if week == 0:
    print('SUN')
if week == 1:
    print('MON')
if week == 2:
    print('TUE')
if week == 3:
    print('WED')
if week == 4:
    print('THU')
if week == 5:
    print('FRI')
if week == 6:
    print('SAT')
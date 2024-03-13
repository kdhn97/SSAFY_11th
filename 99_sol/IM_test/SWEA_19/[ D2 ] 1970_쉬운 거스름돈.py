T = int(input()) # 1
for test_case in range(1, T+1):
    N = int(input()) # 32850

    M = [0] * 8

    M[0] = N // 50000
    M0 = N % 50000

    M[1] = M0 // 10000
    M1 = M0 % 10000

    M[2] = M1 // 5000
    M2 = M1 % 5000

    M[3] = M2 // 1000
    M3 = M2 % 1000

    M[4] = M3 // 500
    M4 = M3 % 500

    M[5] = M4 // 100
    M5 = M4 % 100

    M[6] = M5 // 50
    M6 = M5 % 50

    M[7] = M6 // 10
    M7 = M6 % 10

    print(f'#{test_case}') # #1
    print(*M) # 0 3 0 2 1 3 1 0
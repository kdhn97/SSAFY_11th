a, b, v = list(map(int, input().split()))
# result = (최종 값 - 내려가는 값)=>최종 높이 / (오르는 값 - 내려가는 값)=>매일 오르는 높이
result = (v - b) / (a - b)
# result 값이 4.0이라면 int도 4로 == 같다.
# 하지만 result 값이 4.1이라면 int는 4이기에 다르다
if result == int(result):
    print(int(result))
# 이 경우 + 1을 해준다.
else:
    print(int(result)+1)
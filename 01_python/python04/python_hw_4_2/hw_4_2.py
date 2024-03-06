list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]

rental_list = [
    '장생전',
    '원생몽유록',
    '이생규장전',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]
# 내 풀이
for rental in rental_list:
    if rental not in list_of_book:
        print(f'{rental}은/는 보유하고 있지 않습니다.')

# 반복문은 break로 강제 종료된 것과 아닌 것 구분
for rental in rental_list:
    # 대여하려는 책이 목록에 없으면
    if rental not in list_of_book:
        print(f'{rental}은/는 보유하고 있지 않습니다.')
        # break문은 현재 실행 중인 반복문을 종료
        # 중첩 반복문인 경우엔 모든 반복문 종료는 아니다.
        break
else:
    print('모든 도서가 대여 가능한 상태입니다.')
# Book 객체의 pk가 1인 책을 가져와서 book1 변수에 할당합니다.
book1 = Book.objects.get(pk=1)
# book1의 속성들을 변경합니다.
book1.title = '홍길동전'
book1.author = '허균'
book1.pubdate = '1994-07-25'
book1.price = 3000
book1.adult = False
# 변경된 내용을 저장합니다.
book1.save()

# Book 객체의 pk가 2인 책을 가져와서 book2 변수에 할당합니다.
book2 = Book.objects.get(pk=2) 
# book2의 속성들을 변경합니다.
book2.title = '난중일기'
book2.author = '이순신'
book2.pubdate = '2015-01-21'
book2.price = 0
book2.adult = False
# adult 속성을 다시 True로 변경합니다.
book2.adult = True
# 변경된 내용을 저장합니다.
book2.save()

# Book 객체의 pk가 3인 책을 가져와서 book3 변수에 할당합니다.
book3 = Book.objects.get(pk=3) 
# book3의 속성들을 변경합니다.
book3.title = '세종실록'
book3.author = '이도'
book3.pubdate = '1397-05-15'
book3.adult = False
book3.price = 0
# 변경된 내용을 저장합니다.
book3.save()

# book1의 속성들을 출력합니다.
book1.title
book1.author
book1.pubdate
book1.price
book1.adult

# book2의 속성들을 출력합니다.
book2.title
book2.author
book2.pubdate
book2.price
book2.adult
book2.adult # 이 부분이 중복되어 출력되고 있습니다.

# book3의 속성들을 출력합니다.
book3.title
book3.author
book3.pubdate
book3.adult
book3.price

# 각각의 책 객체를 삭제합니다.
book1.delete()
book2.delete()
book3.delete()

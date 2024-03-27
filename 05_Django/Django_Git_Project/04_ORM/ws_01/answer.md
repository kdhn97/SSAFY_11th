book1 = Book.objects.get(pk=1)
book1.title = '홍길동전'
book1.author = '허균'
book1.pubdate = '1994-07-25'
book1.price = 3000
book1.adult = False
book1.save()

book2 = Book.objects.get(pk=2) 
book2.title = '난중일기'
book2.author = '이순신'
book2.pubdate = '2015-01-21'
book2.price = 0
book2.adult = False
book2.adult = True
book2.save()

book3 = Book.objects.get(pk=3) 
book3.title = '세종실록'
book3.author = '이도'
book3.pubdate = '1397-05-15'
book3.adult = False
book3.price = 0
book3.save()


book1.title
book1.author
book1.pubdate
book1.price
book1.adult

book2.title
book2.author
book2.pubdate
book2.price
book2.adult
book2.adult

book3.title
book3.author
book3.pubdate
book3.adult
book3.price

book1.delete()
book2.delete()
book3.delete()
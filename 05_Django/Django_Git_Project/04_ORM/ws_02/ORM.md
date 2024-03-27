book1 = Book(title='첫번째 책', author='첫번째 책 작가', pubdate='2023-12-12', price=0, adult=False)
book2 = Book(title='두번째 책', author='두번째 책 작가', pubdate='2023-12-12', price=0, adult=False)
book3 = Book(title='세번째 책', author='세번째 책 작가', pubdate='2023-12-12', price=0, adult=False)

books = [book1, book2, book3]

for book in books:
    book.save()

books = Book.objects.all()

for book in books:
    print(book.title)
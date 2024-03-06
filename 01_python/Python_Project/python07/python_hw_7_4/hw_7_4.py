# 아래 클래스를 수정하시오.
class Person:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

    def introduce(self):
        return f'제 이름은 {self.name}이고, 제 나이는 {self.age}입니다.'

person1 = Person("Alice", 25)
print(person1.introduce())
print(Person.count)
def some():
    return False

a = 1
b = '가'
c = [1, 2, 3]
d = range(1, 10)
e = map(int, '123')
f = set()
g = dict()
h = some
i = map(some, [1, 2, 3])

def other(arg):
    print(arg)

def some(func, arg):
    func(arg)
    return None

some(other, '안녕하세요')

a = [1, 2]
b = ['a', 'b']
c = ['ㄱ', 'ㄴ']
d = list('가')
a.append(30)
b.append('c')
c.append('ㄷ')
d.append('나')

class Person:
    def breath(self):
        print('습-하')

p1 = Person()
p2 = Person()
p1.breath()
p2.breath()
p1.name = '허유정'
print(p1.name)
p2.name = '이권민'
print(p2.name)
print(type(p1))
print(isinstance(p1, Person))

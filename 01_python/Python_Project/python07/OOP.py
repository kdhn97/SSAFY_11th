# OOP 객체 지향 프로그래밍
# 객체?
a = 1 # 1 객체
b = '가' # '가' 객체
c = [1,2,3] # [1,2,3] 객체
d = range(1,10) # range 객체
e = map(int, '123') # map 객체
f = set() # set 객체
g = dict() # dict 객체

def some():
    return False
h = some # some 객체

i = map(some, [1,2,3])

def other(arg):
    print(arg)

def some(func, arg):
    func(arg)
    return None
some(other, '안녕하세요')

a = [1,2]
b = ['a','b']
c = ['ㄱ','ㄴ']
d = list('가')
a.append(30)
b.append('c')
c.append('ㄷ')
d.append('나')

class Person:
    def breath(self):
        print('습-하')
p1 = Person() # 인스턴스 p1
p2 = Person() # 인스턴스 p2
p1.breath()
p2.breath()
p1.name = '사람'
print(p1.name)
print(type(p1))
print(isinstance(p1, Person))
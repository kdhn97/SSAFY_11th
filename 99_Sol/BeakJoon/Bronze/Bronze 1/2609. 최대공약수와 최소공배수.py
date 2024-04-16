a, b = map(int, input().split())
A = a
B = b

while B != 0:
    A = A % B
    A, B = B, A

print(a)
print(a * b // A)
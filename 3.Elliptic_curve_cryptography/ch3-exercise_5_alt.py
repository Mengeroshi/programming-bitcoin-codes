from ecc import FieldElement, Point
prime = 223

a = FieldElement(0, prime)
b = FieldElement(7, prime)
x = FieldElement(15, prime)
y = FieldElement(86, prime)
p = Point(x, y, a, b)

for i in range(1,101):
    result = i*p
    print(f"{i}* {p} = {result}")
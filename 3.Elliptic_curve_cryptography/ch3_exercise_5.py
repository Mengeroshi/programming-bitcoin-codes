from ecc import FieldElement, Point
prime = 223

a = FieldElement(0, prime)
b = FieldElement(7, prime)
x = FieldElement(15, prime)
y = FieldElement(86, prime)
p = Point(x, y, a, b)
inf = Point(None, None, a, b)

product = p
count = 1

while product != inf:
    product += p
    count += 1

print(count)
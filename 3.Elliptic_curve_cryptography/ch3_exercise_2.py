from ecc import FieldElement, Point
prime = 223

a = FieldElement(0, prime)
b = FieldElement(7, prime)

p1 = Point(FieldElement(170,prime), FieldElement(142, prime), a, b)
p2 = Point(FieldElement(60,prime), FieldElement(139, prime), a, b)
print(p1+p2)

p1 = Point(FieldElement(47,prime), FieldElement(71, prime), a, b)
p2 = Point(FieldElement(17,prime), FieldElement(56, prime), a, b)
print(p1+p2)

p1 = Point(FieldElement(143,prime), FieldElement(98, prime), a, b)
p2 = Point(FieldElement(76,prime), FieldElement(66, prime), a, b)
print(p1+p2)
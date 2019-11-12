from ecc import FieldElement, Point

prime = 223

a = FieldElement(0, prime)
b = FieldElement(7, prime)

p1 = Point(FieldElement(192,prime), FieldElement(105, prime), a, b)
print(p1+p1)

p2 = Point(FieldElement(47,prime), FieldElement(71, prime), a, b)
print(p2+p2)

p3 = Point(FieldElement(47,prime), FieldElement(71, prime), a, b)
print(p3+p3+p3+p3)

p3 = Point(FieldElement(47,prime), FieldElement(71, prime), a, b)
print(p3+p3+p3+p3+p3+p3+p3+p3)

p3 = Point(FieldElement(47,prime), FieldElement(71, prime), a, b)
print(p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3)

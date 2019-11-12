from ecc import Point

p1 = Point(-1, -1, 5, 7)
#p2 = Point(-1 , -2, 5, 7)

def on_curve(x, y):
    return y**2 == x**3 + 5*x + 7

print(on_curve(2, 4))

print(on_curve(-1, -1))

print(on_curve(18, 77))

print(on_curve(5, 7))
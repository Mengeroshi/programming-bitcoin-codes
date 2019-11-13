from ecc import S256Point, G, N
from helper import hash256
e = 12345
z = int.from_bytes(hash256(b'Programming Bitcoin!'), 'big')
k = 1234567890
r = (k*G).x.num
k_inv = pow(k, N-2, N)
s = (z+r*e) * k_inv % N
print( e*G)
print(hex(z))
print(hex(r))
print(hex(s))
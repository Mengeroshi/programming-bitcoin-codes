from helper import murmur3
from bloomfilter import BIP37_CONSTANT
field_size = 10
num_functions = 5
tweak = 99
bit_field_size = field_size * 8
bit_field = [0] * bit_field_size
for phrase in (b'Hello World', b'Goodbye!'):
    for i in range(num_functions):
        seed = i * BIP37_CONSTANT + tweak
        h = murmur3(phrase, seed=seed)
        bit = h % bit_field_size
        bit_field[bit] = 1
print(bit_field)
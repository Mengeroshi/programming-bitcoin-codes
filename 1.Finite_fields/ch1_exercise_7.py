 

for prime in (7, 11, 17, 31):
    print([pow(i, prime-1, prime) for i in range(1, prime)])
from ecc import PrivateKey
from helper import hash256, little_endian_to_int

passphrase = b'pickmeupimscared1419'
secret = little_endian_to_int(hash256(passphrase)) 
priv = PrivateKey(secret)
print(priv.point.address(testnet=True))
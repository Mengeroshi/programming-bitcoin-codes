from ecc import PrivateKey

priv = PrivateKey(5003)
print(priv.wif(compressed=True, testnet=True))

priv = PrivateKey(2021**5)
print(priv.wif(compressed=False, testnet=True))

priv = PrivateKey(0x54321deadbeef)
print(priv.wif(compressed=True, testnet=False))
from ecc import PrivateKey

priv = PrivateKey(500)
print(priv.point.sec(compressed=False).hex())
print("+"*100)
priv = PrivateKey(2018*5)
print(priv.point.sec(compressed=False).hex())
print("+"*100)
priv = PrivateKey(0xdeadbeeff12345)
print(priv.point.sec(compressed=False).hex())


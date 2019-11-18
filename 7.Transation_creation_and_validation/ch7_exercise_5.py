from ecc import PrivateKey
from helper import decode_base58, SIGHASH_ALL, little_endian_to_int, hash256
from script import p2pkh_script, Script
from tx import TxIn, TxOut, Tx

prev_tx = bytes.fromhex("b480612f587e91b3e45403b4f135de56669b27b4f0e95e1b1bb9419272565e85")
prev_index = 1

prev_tx_a = bytes.fromhex("c1ca8fc501b42aefbe28a276abe797f53d20415a6971512912d0a3b85b06c554")
prev_index_a = 1

target_address = "myxBsPLTwYQXJXbeausiiTHBXodDcX27mR"
target_amount = 0.03

passphrase = b'pickmeupimscared1419'
secret = little_endian_to_int(hash256(passphrase)) 
priv = PrivateKey(secret)

tx_ins = []
tx_ins.append(TxIn(prev_tx, prev_index))
tx_ins.append(TxIn(prev_tx_a, prev_index_a))

tx_outs = []
h160 = decode_base58(target_address)
script_pubkey = p2pkh_script(h160)
target_satoshis = int(target_amount*100_000_000)
tx_outs.append(TxOut(target_satoshis, script_pubkey))


tx_obj =Tx(1,tx_ins, tx_outs, 0, testnet=True)

print(tx_obj.sign_input(0, priv))
print(tx_obj.sign_input(1, priv))
print(tx_obj.serialize().hex())
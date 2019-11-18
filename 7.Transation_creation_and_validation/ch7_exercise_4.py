from ecc import PrivateKey
from helper import decode_base58, SIGHASH_ALL, little_endian_to_int, hash256
from script import p2pkh_script, Script
from tx import TxIn, TxOut, Tx

prev_tx = bytes.fromhex("63fdb36b4ca0140ad343687ad8947a9d3adf9820383aefd9ae4d4c3521dde7dc")
prev_index = 1
target_address = "mwJn1YPMq7y5F8J3LkC5Hxg9PHyZ5K4cFv"
target_amount = 0.01

change_address = "myxBsPLTwYQXJXbeausiiTHBXodDcX27mR"
change_amount = 0.009

passphrase = b'pickmeupimscared1419'
secret = little_endian_to_int(hash256(passphrase)) 
priv = PrivateKey(secret)

tx_ins = []
tx_ins.append(TxIn(prev_tx, prev_index))

tx_outs = []
h160 = decode_base58(target_address)
script_pubkey = p2pkh_script(h160)
target_satoshis = int(target_amount*100_000_000)
tx_outs.append(TxOut(target_satoshis, script_pubkey))

h160 = decode_base58(change_address)
script_pubkey = p2pkh_script(h160)
change_satoshis = int(change_amount*100_000_000)
tx_outs.append(TxOut(change_satoshis, script_pubkey))

tx_obj =Tx(1,tx_ins, tx_outs, 0, testnet=True)
print(tx_obj.sign_input(0, priv))
print(tx_obj.serialize().hex())
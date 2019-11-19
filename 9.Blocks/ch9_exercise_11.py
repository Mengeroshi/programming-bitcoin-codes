from io import BytesIO
from block import Block
from helper import TWO_WEEKS, target_to_bits

block_hex1 = "000000203471101bbda3fe307664b3283a9ef0e97d9a38a7eacd8800000000000000000010c8ab\
a8479bbaa5e0848152fd3c2289ca50e1c3e58c9a4faaafbdf5803c5448ddb845597e8b0118e43a\
81d3"
block_hex2 = "02000020f1472d9db4b563c35f97c428ac903f23b7fc055d1cfc26000000000000000000b3f449\
fcbe1bc4cfbcb8283a0d2c037f961a3fdf2b8bedc144973735eea707e1264258597e8b0118e5f0\
0474"

last_block = Block.parse(BytesIO(bytes.fromhex(block_hex1)))

first_block = Block.parse(BytesIO(bytes.fromhex(block_hex2)))

time_diferencial = last_block.timestamp - first_block.timestamp

if time_diferencial > TWO_WEEKS * 4:
    time_diferencial = TWO_WEEKS *4

if time_diferencial < TWO_WEEKS // 4:
    time_diferencial = TWO_WEEKS // 4
new_target = last_block.target() * time_diferencial // TWO_WEEKS
new_bits = target_to_bits(new_target)
print(new_bits.hex())
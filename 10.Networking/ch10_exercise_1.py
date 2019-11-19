from network import NetworkEnvelope
from io import BytesIO

message_hex = 'f9beb4d976657261636b000000000000000000005df6e0e2'

envelope = NetworkEnvelope.parse(BytesIO(bytes.fromhex(message_hex)))
print(envelope.command)
print(envelope.payload)
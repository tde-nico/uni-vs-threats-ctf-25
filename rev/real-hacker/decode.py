from base64 import b64decode

a = '+SkNNCl+bRZN/2/H+IlzNfN2/zsGC/jFswBVbZcpaaAf7tyEfIVtwM2LABLeNbA5wPAH3ILJqahO3Jqm/sjQn6VwlbQzSyntSP0HoQjtbPozMvsf4aTDLJHzi7czzM8w9TnIL5kaalr27g5cCtunJUZRlz3hbI8GVZBeQrLI5JuQKLhbfzo2TGv8HHjF+E9JHJJbSMgMeX3csyrdcJ2lz13Gyve9KZzvhTgqY+9VSNSNSNSNSNSNS/x22j8UaW+sKyCQf3Cd+HeorifRjD/0i5pfiC3Cy6f1hJRTmBdn15W5pfj8hkDODODODODODODO9lt1m376s/Ib8GZsbwZqicUsbsExV9Eb9wC+YmwZpvZkC14C4ynwjse1/YUhCHpVMl+e/lT1HSo/G4kj17qiUPihMAiA88vXY1Q0yb3cPPsE17uo9+zsii3Kbda/qV/nO7M27s4U+HBUQK85SPbWs89BfJpvvqfzhjxC2bz4MQmnvtLLNvie8OVTe+FiUHrA7QuEpTEeZHunWCuLN+TUYU0uLNQGGar1u7zfIZJTCYZkk3DR9Z7sirEgf1Sje4SG71j00Fk1YRsw3gNe+O22UtWjhlcHMqre5mEpmkiPnb7AUqAfia4S8U306tfL31Tir0pSG5XQ1Dy5vsgCrZ/efPKQcNVMNNN='

def rot13(s):
	result = []
	for c in s:
		if 'a' <= c <= 'z':
			result.append(chr((ord(c) - ord('a') + 13) % 26 + ord('a')))
		elif 'A' <= c <= 'Z':
			result.append(chr((ord(c) - ord('A') + 13) % 26 + ord('A')))
		else:
			result.append(c)
	return ''.join(result)

b = b64decode(rot13(a))

def bit_rotate(value, shift):
	shift %= 8
	return ((value << shift) | (value >> (8 - shift))) & 0xFF

c = bytearray(b)
for i in range(len(c)):
	c[i] = bit_rotate(c[i], 37)

print(c.hex())

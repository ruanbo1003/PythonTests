
import uuid

key = uuid.uuid4()
key_hex = uuid.uuid4().hex



print(key)

print(type(key))  # <class 'uuid.UUID'>

print(key_hex)

k2 = str(key).replace("-", "")
print(k2)


x = uuid.UUID('000102030405060708090a0b0c0d0e0f')
print("x:", x, type(x), x.hex, type(x.hex), str(x))

y = uuid.UUID(f'{key}')
print("y:", y, type(y))

z = uuid.UUID(x.hex)
print("z,", z, type(z))


str = ""

print(not str)

print(str is None)

D = {'a': None}

print(D)

for k, v in D.items():
    print(k, v)
    if v is None:
        D[k] = ""
        print(k, v)

print(D)

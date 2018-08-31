

s = set()

s.add(1)

s.update([1, 3, 4])
s.update([3, 5])

s2 = (3, 5, 6)
s.update(s2)

print(s)
print(1 in s)
# print(s.issubset((1, )))

for i in s:
    print(i)

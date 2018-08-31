
str = "a HelloWorld"

print(str.index("He"))

print(str.find("He"))

if str.find("He"):
    print("find")

if str.find("Wo"):
    print("find 2")

print(str.find("hqhq"))

if "He" in str:
    print("He is in")

if "HE" in str:
    print("HE is in too")

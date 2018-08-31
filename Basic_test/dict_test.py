

def dict_test():
    d = {}

    print("a" in d)  # False

    item = d["a"] if "a" in d else []
    item.append(1)

    d.update({"a":item})

    d["a"] = "aaa"

    print(d)

    print(d.values())

    print("a" in d)  # True


def dict_test2():
    d = {}
    d['a'] = [1,]

    print(d['a'])

    d['a'].append(2)
    print(d['a'])

    d["c"] = 'abcd'

    for i in d:
        print(i)

    for k, v in d.items():
        print(k, v)

    del d['c']

    print(d)


def dict_subset():
    d = {'a': 1, 'b':2,
         'c': 3, 'd': 4}

    print(d.keys(), type(d.keys()), list(d.keys()))

    print(d.items())


if __name__ == "__main__":
    # dict_test2()

    dict_subset()

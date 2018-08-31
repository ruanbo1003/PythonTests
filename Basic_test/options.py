

class Options():
    def __init__(self, id=None, **options):
        print(f"id:{id}")
        print(f"options:{options}")
        pass


def options_test():
    options = {
        'a': 1
    }
    o = Options(1, **options)


if __name__ == '__main__':
    options_test()

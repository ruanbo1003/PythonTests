
import sys

def throw_exception(str):
    try:
        str = "test"
        for i in None:
            print(i)
    # except Exception as ex:
    #     print("catched 1")
    #     raise Exception("catched and raise")
        # print(str)
        # tb = sys.exc_info()[2]
        # raise Exception(ex.args).with_traceback(tb)
    finally:
        print("finally")


if __name__ == "__main__":
    try:
        throw_exception("hello")
    except Exception as ex:
        # print(ex.args)
        # print(dir(ex))
        print("catched 2")
        print(ex)
        print(ex.args)
        # raise ex
    # throw_exception("hello")

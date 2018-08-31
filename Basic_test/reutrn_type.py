
def return_bool() -> bool:
    print("return bool")
    return "123"


if __name__ == "__main__":
    ret = return_bool()
    print(ret, type(ret))

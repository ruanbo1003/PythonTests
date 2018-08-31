# -*- coding: utf-8 -*-


import json
import time

def json_test():
    data = {"type":1, "title":"会议", "address" : "GuangZhou"}
    j_str = json.dumps(data, ensure_ascii=False)
    print(j_str)

    time.sleep(1)

def json_type():
    str = "hello world"
    j = json.dumps(str)
    print(type(j))

    d = {
        "key": "value",
    }

    print(type(json.dumps(d)))

    print(type(json.loads(str)))

    # jl = json.loads(str)
    # print(type(jl))



if __name__ == "__main__":
    # json_test()

    json_type()







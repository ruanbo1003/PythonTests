
import json


def dict_to_string_test():
    d = {
        'dspt': "string.",
        'phones': [
            {
                'region': 'hk',
                'number': 123456,
            }
        ]
    }

    dstr = str(d)
    print(dstr)

    dict_json = json.dumps(d)
    print(type(dict_json))
    print(dict_json)

    d2 = json.loads(dict_json)
    print(f"type(d2):{type(d2)}")
    print(d2)


if __name__ == '__main__':
    dict_to_string_test()

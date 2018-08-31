
import json
from collections import OrderedDict

import deepdiff


def od_sort_test():
    od = OrderedDict([
        (2, OrderedDict([
            ('depth', 10),
            ('height', 51),
            ('width', 51),
            ('id', 100)
        ])),
        (0, OrderedDict([
            ('depth', 1),
            ('height', 51),
            ('width', 51),
            ('id', 48)
        ])),
        (1, OrderedDict([
            ('depth', 2),
            ('height', 51),
            ('width', 51),
            ('id', 55)
        ])),
    ])

    # foo = OrderedDict(sorted(od.items(), key=lambda x: x[1]['depth']))

    print(od)
    # print(foo)

    od.update({"test":1})

    print(od)


def meeting_address_test():
    lod = [
        OrderedDict(
            [
                ('city', 'hong_kong'),
                ('translations', {'zh-hant': OrderedDict([('address', '中信大廈玩2222')]),
                                  'zh-hans': OrderedDict([('address', '中信大厦玩2222')]),
                                  'en': OrderedDict([('address', 'Citic building大师傅')])
                                 }
                )
            ]
        )
    ]

    # print(lod)

    lod2 = [
        OrderedDict(
            [
                ('city', 'hong_kong'),
                ('translations', {'zh-hant': OrderedDict([('address', '中信大廈玩2222')]), 'zh-hans': OrderedDict([('address', '中信大厦玩2222')]), 'en': OrderedDict([('address', 'Citic building大师傅')])})
            ]
        ),
        OrderedDict(
            [
                ('city', 'g2'),
                ('translations', {'zh-hant': OrderedDict([('address', '廣州111')]), 'zh-hans': OrderedDict([('address', '广州111')]), 'en': OrderedDict([('address', 'guangzhou en')])})
            ]
        ),
        OrderedDict(
            [
                ('city', 'g'),
                ('translations', {'zh-hant': OrderedDict([('address', '廣州111')]), 'zh-hans': OrderedDict([('address', '广州111')]), 'en': OrderedDict([('address', 'guangzhou en')])})
            ]
        )
    ]

    lod3 = [
        OrderedDict(
            [
                ('city', 'hong_kong'),
                ('translations', {'zh-hant': OrderedDict([('address', '中信大廈玩2222')]),
                                  'zh-hans': OrderedDict([('address', '中信大厦玩2222')]),
                                  'en': OrderedDict([('address', 'Citic building大师傅')])})
            ]
        ),
        OrderedDict(
            [
                ('city', 'g'),
                ('translations',
                 {
                     'zh-hant': OrderedDict([('address', '廣州111')]),
                     'en': OrderedDict([('address', 'guangzhou en')]),
                     'zh-hans': OrderedDict([('address', '广州111')]),
                 }
                )
            ]
        ),
        OrderedDict(
            [
                ('city', 'g2'),
                ('translations',
                 {
                     'en': OrderedDict([('address', 'guangzhou en')]),
                     'zh-hant': OrderedDict([('address', '廣州111')]),
                     'zh-hans': OrderedDict([('address', '广州111')]),

                 }
                )
            ]
        )
    ]

    lod2 = [dict(item) for item in lod2]
    lod3 = [dict(item) for item in lod3]

    sorted_lod2 = sorted(lod2, key=lambda x: x['city'])
    sorted_lod3 = sorted(lod3, key=lambda x: x['city'])

    # print(len(sorted_lod))

    # od1 = sorted_lod2[0]
    # od2 = sorted_lod2[1]

    # print(od1.items())
    # print(type(od1.items()))

    # print(od1 == od2)

    print(lod2 == lod3)
    print(sorted_lod2 == sorted_lod3)

    print(deepdiff.DeepDiff(lod2, lod3, ignore_order=True))

    if False:
        city1 = OrderedDict(
            [
                ('city', 'hong_kong'),
                ('translations', {'zh-hant': OrderedDict([('address', '中信大廈玩2222')]),
                                  'zh-hans': OrderedDict([('address', '中信大厦玩2222')]),
                                  'en': OrderedDict([('address', 'Citic building大师傅')])})
            ]
        )

        city2 = OrderedDict(
            [
                ('translations', {'zh-hant': OrderedDict([('address', '中信大廈玩2222')]),
                                  'zh-hans': OrderedDict([('address', '中信大厦玩2222')]),
                                  'en': OrderedDict([('address', 'Citic building大师傅')])}),
                ('city', 'hong_kong'),
            ]
        )

        print(city1 == city2)

        print(city1.items())
        print(city1.keys())

        city3 = dict(city1)
        print(city3)


def dict_test():
    d1 = {
        'a': 1,
        'b': 2,
        'c': 3
    }

    d2 = {
        'a': 1,
        'c': 3,
        'b': 2,
    }

    print(d1 == d2)
    print(d1, d2)


if __name__ == "__main__":
    od_sort_test()

    # meeting_address_test()

    # dict_test()



class TranslationFildItem(object):
    values = {
        "zh-hans": None,
        "zh-hant": None,
        "en": None,
    }

    def __getitem__(self, item):
        return self.values[item]

    def __setitem__(self, key, value):
        self.values[key] = value


t = TranslationFildItem()

t['en'] = ['test', ]
print(t["en"])
t['en'].append('13')
print(t.values)

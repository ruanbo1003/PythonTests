

if __name__ == "__main__":
    t = ()

    print("type(t):", type(t))
    if t:
        print("t")

    LANGUAGES = (
        ('zh-hans', 'zh-hans'),
        ('zh-hant', 'zh-hant'),
        ('en', 'en'),
    )

    print(dict(LANGUAGES))

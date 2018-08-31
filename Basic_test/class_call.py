
class CallTest():
    def __init__(self):
        print("CallTest()")
        self.agent = None

    def __call__(self, *args, **kwargs):
        print(args, kwargs)

    def __getattr__(self, item):
        print("item:", item)

    def __getitem__(self, item):
        print(item)

    def agent_call(self, func):
        self.agent.func()


if __name__ == "__main__":
    ct = CallTest()

    ct.show()

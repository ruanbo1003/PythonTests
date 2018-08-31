
class User(object):
    id = 0

    def __init__(self, id):
        self.id = id


user = User(100)

print(user.id)

class Singleton:
    """class Singleton garantee that class created in one instance"""
    isinstance = None

    def __new__(cls, *args, **kwargs):
        if cls.isinstance is None:
            cls.isinstance = super.__new__()
        return cls.isinstance


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return "{},{}".format(self.name, self.email)

    def __hash__(self):
        return hash(self.email)

    def __eq__(self, other):
        return self.email == other.email


    def __getattr__(self, item):
        return 'Nothing found'

    def __getattribute__(self, item):
        return se

Bob = User('ddd', 'dda')
# Bob.name ='ddd'
# Bob.email = 'ss'
print(Bob)

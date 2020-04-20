

class One:
    """this is demo class """
    def __init__(self):
        print(id(self))

ob1=One()
print(id(ob1))
print(One.__doc__)

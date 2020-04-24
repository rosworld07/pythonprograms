
class EvenException(Exception):
    def __init__(self,arg):
        self.arg=arg

class OddException(Exception):
    def __init__(self,arg):
        self.arg=arg


x=int(input("enter any number"))
if x%2==0:
    raise EvenException("even exception")
else:
    raise OddException("odd exception ")


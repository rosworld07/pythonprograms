

class one:

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def fun(self):
        print("fun")
        print(self.a+self.b)
        
    def sum(self, arg1):
        tem=one(0, 0)
        tem.a=self.a+arg1.a
        tem.b=self.b+arg1.b
        return tem



ob1 = one(2, 3)
ob2 = one(6, 7)
ob3 = ob1.sum(ob2)
print(ob3.a, ob3.b)





class One:
    def set(self,id,name):
        self.id=id
        self.name=name

    def dis(self):
        print(self.id)
        print(self.name)


ob1=One()
ob1.set(2,"ros")
ob1.dis()
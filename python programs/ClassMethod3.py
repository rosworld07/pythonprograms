

class Employ:
    def set(self,sid,sname):
        #sid=int(input("enter id of student"))
        self.sid=sid
        #sname=input("enter name")
        self.sname=sname


    def dis(self):
        print(self.sid)
        print(self.sname)


ob1=Employ()
ob1.set(2,"ros")
ob1.dis()


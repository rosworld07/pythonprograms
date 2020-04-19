
d={}
id=1
ch=0
while True:
    print("press 1 to add data in dictionary")
    print("press 2 to add update in dictionary")
    print("press 3 to add delete in dictionary")
    print("press 4 to add dis in dictionary")
    print("press 6 to clear all in dictionary")
    print("press 5 to add exit in dictionary")
    ch=int(input("enter your choice"))
    if ch==1:
        name=input("enter name")
        d[id]=name
        id=id+1
    if ch==2:
        k = int(input("enter id"))
        name = input("enter the name u want to update ")
        d[k] = name
    if ch==3:
        k = int(input("enter id u want to delete"))
        print(d[k])
        del d[k]
    if ch==6:
        d.clear()


    if ch==5:
        break
    if ch==4:
        print(d)










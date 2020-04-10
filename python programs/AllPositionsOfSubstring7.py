s=input("enter string ")
sub=input("enter substring")
pos=-1
flag=False
n=len(s)

#p=s.find(sub)
#print(p)

while True:
    pos=s.find(sub,pos+1,n)
    if pos==-1:
        break
    print("found at pos= ",pos)
    flag=True
if flag==False:
    print("not found")

#counting substring
print(s.count('a'))

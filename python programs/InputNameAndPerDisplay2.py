
n=int(input("enter the number of stud record"))

i=1

d={}

while i<=n:
       name=input("enter the name of student")
       per=input("enter the percentage")
       d[name]=per
       i=i+1

print(d)
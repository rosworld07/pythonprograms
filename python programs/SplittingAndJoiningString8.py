
#spliting string
s=input("enter string ")

l=s.split()    # by default space considered and return list

for x in l:
    print(x)


s="10-02-44"
l=s.split('-')
print(l)

#joining of string
s=input("enter string ")
s1=input("enter second string ")

s.join(s1)
print("joinstring =",s)

t=('sunny','bunny','chinny')
s='-'.join(t)
print(s)





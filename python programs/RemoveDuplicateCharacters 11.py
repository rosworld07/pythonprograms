
#removing duplicate character

s = input("enter any name ")

l=len(s)

li=[]

for x in s:
    if x not in li:
        li.append(x)
output=''.join(li)
print(output)
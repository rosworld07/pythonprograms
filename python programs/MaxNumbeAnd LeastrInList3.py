l=[2, 3, 14, 5, 6]
print(type(l))
s = l[0]
for x in l:
    if x>s :
        s=x;


print("greatest number in list = ",s)

s = l[0]
for x in l:
    if x<s :
        s=x;

print("smallest number in list = ",s)

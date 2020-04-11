
#1 st way

s=input("enter name")

print("even = ", s[0: :2])
print("odd = ", s[1: :2])

#second way

l=len(s)
i=0
print("even pos character")
while i<l:
    print(s[i],end='')
    i=i+2;
print()

i=1
print("odd pos character")
while i<l:
    print(s[i],end='')
    i=i+2;



from array import *

ar = array('i', [])

for i in range(5):
    n = input("enter ")
    ar.append(int(n))

print(ar)
j = i
for i in range(5):

    for j in range(1, j-i):
        print(j)
        if ar[j]> ar[j+1]:
            temp=ar[j]
            ar[j]=ar[j+1]
            ar[j+1] = temp

print(ar)

from array import *

ar = array('i', [])

for i in range(5):
    n = input("enter ")
    ar.append(int(n))

print(ar)

for i in range(5):
    for j in range(i+1,5):
        if ar[i]> ar[j]:
            temp=ar[i]
            ar[i]=ar[j]
            ar[j]=temp

print(ar)




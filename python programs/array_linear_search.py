
from array import *


arr1 = array('i', [])
for x in range(5):
    n = input("enter array")
    arr1.append(int(n))

print(arr1)

s = int(input("enter the number u want to search"))
f=0
for x in range(5):
    print(arr1[x])
    if arr1[x] == s:
        print(f)
        f = 1


if f == 1:
    print("present ")
else:
    print("not present")

from array import *


arr1 = array('i', [])
for x in range(5):
    n = input("enter array")
    arr1.append(int(n))

print(arr1)

s = input("enter the number u want to search")
for x in range(5):
    if arr1[x] == s:
        f = 1


if f == 1:
    print("present ")
else:
    print("not present")
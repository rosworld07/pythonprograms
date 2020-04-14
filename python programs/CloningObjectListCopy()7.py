

l1=[1,2,3,4,5,6]
l2=l1; #The process of giving another reference variable to the existing list is called aliasing
print(l1)
print(l2)
l2[3]=34  # after changing one both will change
print(l1)
print(l2)

# soln for this is copy function
l1.clear()
l2.clear()
l1=[2,3,4,5,6,7]
print(l1)
l2=l1.copy()
print(l2)
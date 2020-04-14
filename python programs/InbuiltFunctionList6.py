
s=[4,5,9]

s.append(23) # add element at last
print(s)
s.insert(2,45)  # insert at specifig index
print(s)

order1=["Chicken", "Mutton", "Fish"]
order2=["RC", "KF", "FO"]
order1.extend(order2)  #copying one list to another

print(order1)

s.remove(45)  #remove the value
print("after removing 45", s)

s.pop();
print("after removing  using pop", s)

s.reverse()
print("after reversing", s)

n=[20,5,15,10,0]
n.sort()
print("after sorting",n)

s=["Dog","Banana","Cat","Apple"]
s.sort()
print("after sorting",s)


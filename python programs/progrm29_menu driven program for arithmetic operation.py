#menu driven program for arithmetic operation

print("press 1 for add")
print("press 2 for sub")
print("press 3 for mul")
print("press 4 for div")
ch=int(input("enter your choice"))
if ch==1:
  
  num1=int(input("enter num1"))
  num2=int(input("enter num2"))
  res=num1+num2
  print("addition ="+str(res))
elif ch==2 :
  
  num1=int(input("enter num1"))
  num2=int(input("enter num2"))
  res=num1-num2
  print("sub ="+str(res))
elif ch==3:
  
  num1=int(input("enter num1"))
  num2=int(input("enter num2"))
  res=num1*num2
  print("mul ="+str(res))
elif ch==4 :
  
  num1=int(input("enter num1"))
  num2=int(input("enter num2"))
  res=num1/num2
  print("div ="+str(res))
else :
  print("not valid choice")

  
   

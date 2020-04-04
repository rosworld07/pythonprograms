#menu driven program for arithmetic operation using +,-,/,*

print("press + for add")
print("press - for sub")
print("press * for mul")
print("press / for div")
ch=input("enter your choice")
if ch=="+":
  
  num1=int(input("enter num1"))
  num2=int(input("enter num2"))
  res=num1+num2
  print("addition ="+str(res))
elif ch=="-" :
  
  num1=int(input("enter num1"))
  num2=int(input("enter num2"))
  res=num1-num2
  print("sub ="+str(res))
elif ch=="*":
  
  num1=int(input("enter num1"))
  num2=int(input("enter num2"))
  res=num1*num2
  print("mul ="+str(res))
elif ch=="/" :
  
  num1=int(input("enter num1"))
  num2=int(input("enter num2"))
  res=num1/num2
  print("div ="+str(res))
else :
  print("not valid choice")

  
   

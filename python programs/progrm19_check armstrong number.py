# check armstrong number




num =int(input("enter 3 digit number"))
org_num=num

n1=int(num%10);
num=num/10;
n2=int(num%10);
num=num/10;
n3=int(num%10);
res=int(n1*n2*n3)


if org_num == num:
  print("armstrong")
else:
  print("not armstrong")




  

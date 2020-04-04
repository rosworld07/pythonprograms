# program to enter n digit and check armstrong



rev=0
num = int(input("enter any number"))
org_num=num
while num>0:
  d1=int(num%10)
  num=int(num/10)
  rev=rev+(d1*d1*d1);
print(rev)
if org_num==rev :
  print("armstrong")
else :
  print("not armstrong")
  
  
   

# program to enter  nd perfom addition on n digit



rev=0
num = int(input("enter any number"))
while num>0:
  d1=int(num%10)
  num=int(num/10)
  rev=rev+d1;
print(rev)
  
  
   

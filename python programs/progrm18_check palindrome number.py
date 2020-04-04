# check palindrome number




num =int(input("enter 3 digit number"))
org_num=num

n1=int(num%10);
num=num/10;
n2=int(num%10);
num=num/10;
n3=int(num%10);
rev=int(n1*100+n2*10+n3)


if org_num == num:
  print("palindrome")
else:
  print("not palindrome")




  

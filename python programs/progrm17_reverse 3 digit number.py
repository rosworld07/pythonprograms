# reverse 3 digit number




num =int(input("enter 3 digit number"))


n1=int(num%10);
num=num/10;
n2=int(num%10);
num=num/10;
n3=int(num%10);
rev=int(n1*100+n2*10+n3)

print("reverse ="+str(rev))




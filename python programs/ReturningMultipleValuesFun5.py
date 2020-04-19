#returning multiple values from function 
def fun(x,y):
    a=x+y
    b=x-y
    return a,b

r1,r2=fun(2,3)
print(r1,r2)
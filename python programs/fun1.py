
def fun1():
    print("hellow")


fun1()

#passing parameter

def fun2(x):
    print(x)

fun2(34)

#pass and return from fun

def fun3(x,y):
    return x+y

s=fun3(4,5)
print(s)

#if returning nothing it return none
def fun4():
    print("hi")

print(fun4())
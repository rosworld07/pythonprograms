import  os
a=10


try:
    x = a / 0
except Exception as msg:
    print(msg)
    os._exit(0)  #finally not executed
finally:
    print("finally executed")


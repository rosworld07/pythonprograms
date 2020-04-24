a=10


try:
    x = a / 7
except Exception as msg:
    print(msg)
finally:
    print("finally executed")


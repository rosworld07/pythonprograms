try:
    x=int(input("Enter First Number: "))
    y=int(input("Enter Second Number: "))
    print(x/y)
except (ZeroDivisionError,ValueError) as msg :
    print("exception ",msg)

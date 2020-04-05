s =input("enter name")

if len(s) <= 2:
    print("empty")
else:

    s2 = s[: 2] + s[-2:]
    print(s2)

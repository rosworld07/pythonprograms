


str1= input("enter name")
char = str1[0]
str1 = str1.replace(char, '$')
str1 = char + str1[1:]

# ch=s[0]
# s=s.replace(ch,'$')
print(str1)

s="python by roshan kumar"

#by index
for i in range(len(s)):
    print(s[i])
#using for each
for x in s:
    print(x)

#by slice operator

print(s[0:len(s)]) # 0 to end -1
print(s[0:])      #by default end
print(s[:])       #by default start and end 0 to -1
print(s[::-1])     #display i reverse if step is minus
print(s[::2])       #increment by 2 position 

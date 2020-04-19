
#creating empty dictionary
d=dict()
print(type(d))

d={12:"ram",2:"shyam"}

print(d[12])  #accessing by key value
print(d[2])

for x in d:
    print(x)  #getting key value
    print(d[x])  #getting data of key value

#updating data

d[12]="update name"

print(d)

d2={"a":"ram","b":"shyam"}
print(d2)

t = (10, 20, 30, 40,10)
print(len(t)) # find length

#count()

print(t.count(10))


#sorted

t=sorted(t)

print(t)

#sorted in reverse
t=sorted(t,reverse=True)
print(t)

#min and max function

m=min(t)
print("minimum value in tuprl=",m)

m=max(t)
print("maximum value in tuprl=",m)

t1 = (10, 20, 30)
t2 = (40, 50, 60)
t3 = (10, 20, 30)
print(cmp(t1, t2))
print(cmp(t1,t3))
print(cmp(t2,t3))  

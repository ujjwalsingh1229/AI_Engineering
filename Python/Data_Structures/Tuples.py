t = (2,3,4,5,6,7,12,5,6,9,10) #initial tuple
print(type(t))
print(t[9])

index = t.index(5) # find the index of first occurence of 9
print(index)

count = t.count(5) # count occurence of 5
print(count)

for i in t: # when we have to print values inside the tuple
    print(i)

for r in range(len(t)): # when we have to print index 
    print(r)

x,y,z,w = (23,34,45,56)
print(x)
print(z)

r =(1)
print(type(r))

s = (2,)
print(type(s))

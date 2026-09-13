d = {}
print(type(d))

d = {1:'ujju' ,3:'singh',2: 'hello'} # key value pair in dictionary using colons ':'
print(type(d))
print(d[1])

# CRUD operation on dict

e = {10: 100,20:200,30:300,40:400,50:500}

print(e[40])

e[10] = 1000 #updating
print(e[10])

e.update({60:600}) #Creating
print(e)

del e[30] #del
print(e)

for i in e:
    print(e[i]) # for value 
    print(i)    # for key 

a = e.clear()
print(a)

# DEEP  copy in list same as also in dict  

p = [1,2,3,4,5]

q = p

q[0] =100

print(p)

e2 =p.copy()
print(e2)

d = {10: 100,20:200,30:300,40:400,50:500}
print(d.items())

d1 ={10:100,20:200,30:300}
d2 ={40:400,50:500,60:600}

for i in d2:
    d1[i] = d2[i]

print(d1)
print(d2)

#Q1 Write a python script to merge two python  dictionaries 
d1 ={10:100,20:200,30:300}

sum = 0
for i in d1:
    sum = sum + d1[i]
print(sum)

#Q2 Write a python program to sum all the values in a dictionary.

w = [1,1,2,2,3,1,2,1,3,4,5,5,5,4,4,4,2,1,1,1,1] # for a list 

count = 0
for i in w:
    if i ==1:
        count += 1
print(count)

d ={}
for i in w:
    if i in d.keys():
        d[i] +=1
    else:
        d[i] = 1

print(d)
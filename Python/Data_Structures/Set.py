s = {2,3,"hii",4,5,6,8,"hello",8}
print(type(s))
print(s)

b = hash("Hello")
print(b)

c = hash((1,2,344))
print(c)

for i in s:
    print(i)

s.add(10) # Adds an element to the set 
print(s)
s.remove(8) # removes 8 (no effror if not found)
print(s)
s.discard(5) # removes a random element
print(s) 
popped_element = s.pop()
print(popped_element)
s.clear() # Removes all elements
print(s) 

a = {1,2,3,4,5,6}
b = {4,5,6,7,8,9}

union_set = a.union(b)
print(union_set)

intersection_set = a.intersection(b)
print(intersection_set)

difference_set = a.difference(b)
print(difference_set)

symmetric_diff = a.symmetric_difference(b)
print(symmetric_diff)

#shortcut symbols for methods 

s = a|b   # pip operator for union
print(s)

t = a & b # and for intersection
print(t)

u = a - b # subtraction operator for difference
print(u)

v = b^a # symmetric difference power operation also called 
print(v)

# COMPOUND OPERATIONS ON SET 

b -= a
print(b)
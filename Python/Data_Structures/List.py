# LIST 

fruits = ["apple" , "orange" , "banana","cherry"]

marks = [23,34,25,27,35,39,45,34]

a = 12,13,14,15,12# stored in a form of tuple data strcture

print(a)

b = [12,13,14,12,15,16,17,34.5,print(),True,False]

# modify the value

b[3] = 'UJJU'

print(b[3])

print(marks[0:5])
print(fruits[0:3])
print(a[0:1])
print(b[0:7:3])
print(b[0:7])

b.remove(12)
print(b)

# list way using index

for i in range(len(b)):
    print(b[i])

#2nd way directly on values

for i in b:
    print(i)




# now we apply some operations on the list such as :
print(dir(list))

numbers = [5,2,9,1,5,6] # initial list 
print(numbers)
numbers.append(10) # Adds 10 to the end 
print(numbers)
numbers.insert(2,15) # Inserts 15 at index 2
print(numbers)
numbers.extend([20,25,30]) # ADDS Multiple elements at the end 
print(numbers)
numbers.remove(5) # Removes the first occurence of 5
print(numbers)
popped_item = numbers.pop(3) # removes and stores the elementat index 3
print(numbers)
index = numbers.index(6) # Finds the index of 6
print(numbers)
count_5 = numbers.count(5) # counts occurence of 5
print(numbers)
numbers.sort() # sorts lists in ascending order
print(numbers)
numbers.reverse() # reverse the list order
print(numbers)
new_numbers = numbers.copy() # Creates  a copy of the list 
print(numbers)
numbers.clear() # removes all element from the list 
print(numbers)

l =[1,2,3,2,4,5]
l[0] = 10
print(l)


# questions practice

#Q1 PRINT positive and negative elements of an list 

s = [ -34,-56,54,65,-67,87,98]

for i in s:
    if i >= 0:
        print("postive element in this list s is ", i)
for i in s:
    if i <  0:
        print("negative  element in this list is ",i)

#Q2 Mean of list element 

r = [23,34,45,56,22]
sum = 0;

for i in r:
    sum = sum + i
print("mean of this list is ",sum/len(r))

#Q3 Find the greatest element and print its index too..

l = [12,36,14,19,128,8,13,29,34,56,78,90]
greatest = l[0]
index    = i 

for i in range(len(l)):
    if l[i] > greatest:
        greatest = l[i]
        index = i

print(f"your greatest number is {greatest} at index {index}")

#Q4 Find the second greatest element.
m = [12,16,13,17,19]

largest = m[0]
secondlargest = m[0]

for i in m :
    if i > largest:
        secondlargest = largest
        largest = i
    elif i > secondlargest:
        secondlargest = i

print(secondlargest , largest)

#Q5 Check list is sorted or not 

x = [10,13,14,15,16]

for i in range(len(x)-1):
    if x[i] < x[i+1]:
        continue
    else:
        print("your list is not ssorted")
        break
else:
    print("your list is sorted")



    


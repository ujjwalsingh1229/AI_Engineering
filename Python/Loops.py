print("ujjwal singh ")
print("ujjwal singh ")
print("ujjwal singh ")
print("ujjwal singh ")
print("ujjwal singh ")
print("ujjwal singh ")
print("ujjwal singh ")
print("ujjwal singh ")
print("ujjwal singh ")
print("ujjwal singh ")
print("ujjwal singh ")
print("ujjwal singh ")
print("ujjwal singh ")
print("ujjwal singh ")
print("ujjwal singh ")
print("ujjwal singh ")
print("ujjwal singh ")
print("ujjwal singh ")
print("ujjwal singh ")
print("ujjwal singh ")
print("ujjwal singh ")
print("ujjwal singh ")
print("ujjwal singh ")
print("ujjwal singh ")
print("ujjwal singh ")
print("ujjwal singh ")
print("ujjwal singh ")
print("ujjwal singh ")
print("ujjwal singh ")
print("ujjwal singh ")
print("ujjwal singh ")
print("ujjwal singh ")
#it is manual print statement but we can use loop to print it multiple times
for i in range(10):
    print("ujjwalsingh ")

# for loop is used to repeat a block of code multiple times. In this case, it will print "ujjwalsingh" 10 times.

a = range(1,21,1)

for i in range(25):
    print(i)

for j in range(20,51):
    print(j)

for k in range(16,1,-1):
    print(k)

for l in range(-5,-16,-1):
    print(l)

for m in range(5,51,5):
    print(m)

"""n = int(input("which table you want to print : "))
for i in range(n,(n*10)+1,n):
    print(i)"""


w = "UJJWAL READS HINDI BOOKS"
print(len(w))

for i in range(len(w)):
    print(w[i])

for j in range(1,21):
    if j == 18:
        break
    else:
        print(j)

for j in range(1,21):
    if j == 18:
        continue
    else:
        print(j)

for r in range(1,24):
    if r == 17:
        print("break statement is executed")
        break
    print(r)

else:
    print("break statement is not executed")


#Q1 Accept an integer and print hello world n times.

n = int(input("enter a number : "))

for i in range(1,n+1):
    print("hello world")

#Q2 Print natural number up to n 

for j in range(1,n+1,1):
    print(j)

#Q3 Reverse for loop print n to 1

for t in range(n,0,-1):
    print(t)

#Q4 sum up to n terms 
sum = 0 

for r in range(1,n+1):
    sum += r

print(f"sum is {sum}")
    

#Q5 factorial of number 
if n < 0 :
    print("Factorial does not exist for negative numbers. ")
else :
      results = 1
      for f in range(1,n+1):
        results *= f
      print(f"factorial is {results}")


#Q6 Print the sum of all even and odd numbers in a range separately.
even_sum = 0
odd_sum = 0
for e in range(0,n+1,2):
    even_sum += e
print("sum of all even number is : " , even_sum)

for o in range(1,n+1,2):
    odd_sum += o
print("sum of all odd number is : ", odd_sum)

#Another method 

even = 0 
odd  = 0

for i in range(1,n+1):
    if i%2 == 0:
        even = even + i
    else :
        odd = odd + i 
print(f"your even and odd sum are {even} , {odd}")            
        

#Q7 Find all the factors of a number.

for f in range(1,n+1):
    if n%f== 0:
        print(f)

#Q8 Accept a number and check if it a perfect number or not. A number whose sum of factors is equal to the number itself

n = int(input("check your number is perfect or not : "))
sum = 0
for i in range(1,n):
    if n % i == 0 :
        sum = sum + i 
if sum == n:
    print("number is perfect")
else:
    print("number is not a perfet")

#Check whether the number is prime or not 
count = 0
for i in range(1,n+1):
    if n % i == 0 :
        count = count + 1

if count == 2:
    print("number is prime ")
else:
    print("number is not prime")

#Q9 Reverse a string 

a = "naman"

for i in range(len(a)-1,-1,-1):
    print(a[i])

b = ""
for i in range(len(a)-1,-1,-1):
    b = b + a[i]
if b == a :
    print("your string is pallindrome")

else:
    print("its not a pallindrome")


print(b)

c = "ujs1229876iwnnn@#$^&&@"

char  = 0 
dig = 0
spchar = 0

for i in c :
    if i.isdigit():
        dig +=1
    elif i.isalpha():
        char+=1
    else:
        spchar +=1
print(f"Your digits are {dig}\nyour albhabets are {char}\nyour special character are {spchar}")

print(dir(str))
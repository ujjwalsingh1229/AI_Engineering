print("hello ! my name is ujjwal singh") #it is built in print function of python

#now we use define function with using def keyword create a function such as :

def hello():
    print("this is hello function so im doing hello")

hello()

#functions parameter and arguments 

def sum(a,b):
    print(f"The sum of your number is {a + b}  ")

sum(23,33)
sum(45,45)

#Types of arguments 

def add(a , b):
    return a + b

print(add(3,5)) #  3 is assigned to 'a' , 5 to 'b'

def introduce(name , age):
    print(f"I am {name} and I am {age} years old.")

introduce(age = 23 , name= 'Ujjwal')   # key value arguments 

def greet(name = 'Guest'):
    print(f"Hello, {name}!")

greet() #Uses default value "Guest"
greet("UJJU") #USES "UJJU"


def pallindrome(st):
    rev = ""
    for i in range(len(st)-1,-1,-1):
        rev = rev + st[i]

    if rev == st:
        print("pallindrome")
    else:
        print("not a pallindrome")

pallindrome("NAMAN")
pallindrome("CURSOR")
pallindrome("UJJU")

#WHAT IS RETURN AND PRINT 

def hello():
    return "hello how are you"

hello()
print(hello())
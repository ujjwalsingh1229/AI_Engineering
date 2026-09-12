# IF ELSE STATEMENT

u = 29
if u > 30:
    print("u is greater than 30")
else:
    print("u is not greater than 30")

a = 20
if a > 25:
    print('i will do task A')
else :
    print('i will do task B')


"""money = int(input("please provide me the money : "))

if money==10:
    print("i will buy a chocobar icecream")

elif money==20:
    print("i will have a mango dolly icecream")

else: 
    print("i will have a vanilla icecream") """

#Q1 Accept two numbers and print the greatest between them 

"""num1 = int(input("enter first number : "))
num2 = int(input("enter second number : "))

if num1> num2:
    print(num1,"is greater than num2")
elif num1==num2:
    print(num1,"is equal to num2")
else:
    print(num2,"is greater than num1")"""

#Q2 Accept the gender from the user as char and print the respective greeting message 
  #eg = Good morning sir for male and good morning ma'am for female

"""gender = input("please enter your gender m/f : ")

if gender == 'm' :
    print(" Good morning sir ")
else :
    print(" Good morning ma'am") """

#Q3 Accept an integer and check whether it is an even number or odd number.

"""num = int(input("enter a number : "))

if num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")"""

#Q4 Accept the name and age of person and check whether he / she valid voter or not.

"""NAME = input("Please enter your name : ")
AGE = int(input("Please enter your age : "))

if AGE >= 18:
    print("hello" ,NAME, "you are  a valid voter")
else:
    print("hello" ,NAME, "you are not a valid voter")"""

#Q5 Accept a year and check if it a leap year or not (google to find out which is leap year and which is not).

"""year = int(input("please enter a year : "))

if year % 100== 0 and year % 400 == 0:
    print(year, "is a leap year")
elif year%4 == 0 :
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")"""

# if elif ladder 

temp = int(input("please enter the temperature : "))
if temp < 0 :
    print("Freezing weather")
elif temp >= 0 and temp < 10 :
    print("Very Cold weather")
elif temp >= 10 and temp < 20 :
    print("cold weather")
elif temp >= 20 and temp < 30 :
    print("Normal in temperature")  
elif temp >= 30 and temp < 40 :
    print("Its Hot")
else:
    print("Its Very Hot")
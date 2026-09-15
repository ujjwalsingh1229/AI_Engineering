
print("hello world")
#print(10/0)  #zero division error 
#print("ujjwal") #exception handling

a = int(input("tell your number : "))

try:
    print(10/a)

except Exception as err:
    print(f"sorry there is an err as {err}")

else:
    print("good there is no exception")

finally:
    print("i will run no matter what")

print("ok i have done the division")

age = int(input("tell me your age : "))
try:

    if age < 10 or age > 18:
       raise ValueError("Your age must be between 10 and 18")
    else:
        print("Welcome to the club")
except Exception as err:
    print(f"an error ocurred as {err}")

print("the club will start soon")
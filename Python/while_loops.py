a = 1

while a <= 10 :
    print(a)

    a = a + 1

a = int(input("tell your number "))

rev = 0


while a > 0:
    rev = rev * 10 + a % 10
    
    a = a // 10
print(rev)

# check pallindromic number

rev = 0
copy = a


while a > 0:
    rev = rev * 10 + a % 10
    
    a = a // 10

if copy == rev:
    print("pallindromic number ")
else:
    print("not a pallindromic number ")

import random 

num = random.randint(1,10)
tries = 0
while True:

    guess = int(input("please guess your number : "))

    if num == guess:
       print("you are right ")
    elif num < guess:
        print("go a little lower")
    elif num > guess:
        print("go a little higher")
    else:
       print("sorry! you are wrong")
print(num)
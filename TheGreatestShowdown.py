# Task 1: Identify the Greatest
number1 = int(input("input your first number"))
number2 = int(input("input your second number"))
number3 = int(input("input your third number"))

if (number1 >= number2) and (number1 >= number3):
    print (f"{number1} is the largest number")
elif (number2 >= number1) and (number2 >= number3):
    print (f"{number2} is the largest number")
else: 
    print(f"{number3} is the largest number")

# Task 2: identify the Smallest

if (number1 <= number2) and (number1 <= number3):
    print (f"{number1} is the smallest number")
elif (number2 <= number3) and (number2 <= number1):
    print (f"{number2} is the smallest number")
else: 
    print(f"{number3} is the smallest number")


# Task 3: Equality Check
    
if (number1 == number2) and (number1 == number3):
    print ("all numbers are equall")
elif (number2 == number3) and (number2 > number1):
    print ("Two Numbers are equall and the largest")
elif (number1 == number3) and (number1 > number2):
    print ("Two Numbers are equall and the largest")
elif (number1 == number2) and (number1 > number3):
    print ("two numbers are equal and the largest")
elif (number2 == number3) and (number2 < number1):
    print ("Two Numbers are equall and the smallest")
elif (number1 == number3) and (number1 < number2):
    print ("Two Numbers are equall and the smallest")
elif (number1 == number2) and (number1 < number3):
    print ("two numbers are equal and the smallest")
else:
    print("none of the numbers entered are equal")

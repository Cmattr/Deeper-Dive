# Task 1: Identify the Greatest
Number1 = int(input("input your first number"))
Number2 = int(input("input your second number"))
Number3 = int(input("input your third number"))

if (Number1 >= Number2) and (Number1 >= Number3):
    print (f"{Number1} is the largest number")
elif (Number2 >= Number1) and (Number2 >= Number3):
    print (f"{Number2} is the largest number")
else: 
    print(f"{Number3} is the largest number")

# Task 2: identify the Smallest

if (Number1 >= Number2) and (Number1 <= Number3):
    print (f"{Number1} is the smallest number")
elif (Number2 <= Number3) and (Number2 <= Number1):
    print (f"{Number2} is the smallest number")
else: 
    print(f"{Number3} is the smallest number")


# Task 3: Equality Check
    
if (Number1 == Number2) and (Number1 == Number3):
    print ("all numbers are equall")
elif (Number2 == Number3) and (Number2 > Number1):
    print ("Two Numbers are equall and the largest")
elif (Number1 == Number3) and (Number1 > Number2):
    print ("Two Numbers are equall and the largest")
elif (Number1 == Number2) and (Number1 > Number3):
    print ("two numbers are equal and the largest")
else:
    print("none of the numbers entered are equal")
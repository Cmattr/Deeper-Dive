# Task 1: Leap year Checker

year =int (input("what year would you like to check"))
century = year // 100 +1
if year % 4 == 0:
    print (f"{year} is a leap year")
else:
    print (f"{year} year is not a leap year")


# Task 2: Century Varification
    
century = year // 100 +1
print (f"{year} is in the {century} century")

# Task 3: Time Traveler

if year > 2024:
    print ("This year is in the future")

elif year == 2024:
    print ("This year is the current year")

else:
    print ("This year is in the past")

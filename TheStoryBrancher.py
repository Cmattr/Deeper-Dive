# Task 1: Code Correction

# The user input needs to be identified as an int
choice = str (input("Do you choose the path to the left or right? "))

# The vairable "Choice" is already set by user input, use == to determine if the user input is equall to the if statement parameters
if choice == "left":
    print("You find a treasure chest!")
# The vairable "Choice" is already set by user input, use == to determine if the user input is equall to the elif statement parameters
elif choice == "right":
    print("You encounter a dragon!")
else:
    print("Invalid choice!")
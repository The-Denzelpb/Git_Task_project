# This is a Github project Task program

# This function does multiplications on two user inputted numbers
def simple_calculator():
    
    # These variables take user input to be used in the calculations
    num = float(input("\nPlease enter a number you wish to multiply: "))
    choice = float(input("Please enter the number you wish to multiply your previous number by: "))

    # This try-except block excepts value errors from the user
    # "return" ensures that the program does not proceed with the calculation after it catches the error 
    try:
        num = float(num)
        choice = float(choice)

    except ValueError:
        print("Please enter a valid number")
        return
    
    # This variable stores the answer the user wants
    value = num * choice
    
    # This print statement, prints the answer in a friendly fashion
    # ":.1f" ensures that the output floats are limited to ONE decimals
    print(f"The number {num:.1f} multiplied by {choice:.1f} is: {value:.1f}\n")


# Get input from the user and store it in a variable (user's name)
name = input("\nPlease enter your name: ")

# Display the information to the user (Welcome message)
print(f"\nWELCOME {name}! Isn't Git Awesome!")

# This variable is the main menu option displayed to the user
# ".lower()" converts user input to lowercase to prevent errors
option = input(f"""\nWhat do you want to do:
Enter A for a multiplication calculator
Enter B to exit the program: """).lower()

# This control block controls the menu option
if option == "a":
    simple_calculator()

elif option == "b":
    exit(f"\nThank You, Goodbye\n")

else:
    print(f"\nInvalid option\n")

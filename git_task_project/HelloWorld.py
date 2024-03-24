def simple_calculator():
    num = float(input("\nPlease enter a number you wish to multiply (can multiply from 2-5 times): "))
    choice = input("""Please pick an option: 
    1 to multiply your number by (2) 
    2 to multiply your number by (3)
    3 to multiply your number by (4)
    4 to multiply your number by (5): """)

    try:
        num = float(num)
        choice = int(choice)

    except ValueError:
        print("Please enter a valid number")

    if choice == 1:
        value = num * 2
        print(f"\nYour number times (2) is: {value}\n")

    elif choice == 2:
        value = num * 3
        print(f"\nYour number times (3) is: {value}\n")

    elif choice == 3:
        value = num * 4
        print(f"\nYour number times (4) is: {value}\n")

    elif choice == 4:
        value = num * 5
        print(f"\nYour number times (5) is: {value}\n")

    else:
        print("\nOption is out of range")


# Get input from the user and store it in a variable.
name = input("\nPlease enter your name: ")

# Display the information to the user
print(f"\nWELCOME {name}! Isn't Git Awesome!")

option = input(f"""\nWhat do you want to do:
Enter A for a simple calculator: """).lower()

if option == "a":
    simple_calculator()

else:
    exit("Thank You, Goodbye")

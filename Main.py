'''
Author: Luke Low
Title: Ultimate Conversion
Date: 7/11/25
Version 1.0
'''

# Variable error message for all general questions with options
option_error = "That is not a valid option, please enter one of the options as provided.\n"

# Asks for type of conversion they want to do
def conversion_type():

    while True:
        
        conversion = str(input('\nPlease enter the type of conversion you want to do, "distance", "mass", "time", or "volume": '))

        if conversion == "distance" or conversion == "mass" or conversion == "time" or conversion == "volume":
            type = conversion
            print(type)
            break

        else:
            print(option_error)


# Asks for the amount they want to convert
def amount():
    amount_error = "That is not a valid number. Please enter a number more than zero next time.\n"

    while True:
        try:
            amount = float(input("Please enter the amount you want to convert: "))
            
            if amount > 0:
                break

            else: 
                print(amount_error)
            
        except ValueError:
            print(amount_error)

    return(amount)

# Asks for starting unit
def start_unit():
    
    while True:
        
        conversion = str(input('\nPlease enter the conversion you want to do, "distance", "mass", "time", or "volume": '))

        if conversion == "distance" or conversion == "mass" or conversion == "time" or conversion == "volume":
            type = conversion
            print(type)
            break

        else:
            print(option_error)


# MAIN PROGRAM

# Welcome message
print("\nWelcome to my Ultimate Conversion program !!\n")

# Asks for instructions or not
instruct = input("Press <enter> to see the instructions or any other key to skip.\n")

# Prints the instructions if user presses <enter>
if instruct == "":
    print("INSTRUCTIONS:")
    print('1. Say which type of conversion you want to do. Eg. "distance", "mass", "time", or "volume".')
    print('2. Enter the amount you want to convert. Eg. "500".')
    print('3. Enter the starting unit of measurement. Eg. "metres".')
    print('4. Enter the ending conversion. Eg. "centimetres".')
    input("\nPress <enter> to continue. ")

else:
    print()

# Runs the input questions
conversion_type()
amount()
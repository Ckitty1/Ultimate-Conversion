'''
Author: Luke Low
Title: Ultimate Conversion
Date: 12/11/25
Version: FINAL
'''



# General variable error messages
option_error = "That is not a valid option, please enter one of the options as provided.\n"
amount_error = "That is not a valid number. Please enter a number more than zero next time.\n"


# Asks for type of conversion they want to do
def conversion_type():

    while True:
        
        # Asks for type of conversion
        conversion = str(input('\nPlease enter the type of conversion you want to do, "distance", "mass", "time", or "volume": '))

        # Checks for invalid answers
        if conversion == "distance" or conversion == "mass" or conversion == "time" or conversion == "volume":
            return(conversion)
            break

        else:
            print(option_error)


# Asks for the amount they want to convert
def ask_amount():

    while True:
        try:
            # Asks for a float amount
            amount = float(input("Please enter the amount you want to convert: "))
            
            # Checks that it's above 0
            if amount > 0:
                return(amount)
                break

            else: 
                print(amount_error)
            
        # Checks errors
        except ValueError:
            print(amount_error)


# Asks for starting unit
def start_unit():
    
    while True:
        
        # Asks for starting unit for distance
        if type == "distance":
            start = str(input('Please enter your starting unit of measurement, "mm", "cm", "m", or "km": '))
            # Checks for invalid answers
            if start == "mm" or start == "cm" or start == "m" or start == "km":
                return(start)
                break
            else:
                print(option_error)

        # Asks for starting unit for mass
        elif type == "mass":
            start = str(input('Please enter your starting unit of measurement, "mg", "g", "kg", or "t": '))
            # Checks for invalid answers
            if start == "mg" or start == "g" or start == "kg" or start == "t":
                return(start)
                break
            else:
                print(option_error)

        # Asks for starting unit for time
        elif type == "time":
            start = str(input('Please enter your starting unit of measurement, "ms", "sec", "min", "hr", "day", "wk", "mth", or "yr": '))
            # Checks for invalid answers
            if start == "ms" or start == "sec" or start == "min" or start == "hr" or start == "day" or start == "wk" or start == "mth" or start == "yr":
                return(start)
                break
            else:
                print(option_error)

        # Asks for starting unit for volume
        elif type == "volume":
            start = str(input('Please enter your starting unit of measurement, "mL", "L", "kL", or "ML": '))
            # Checks for invalid answers
            if start == "mL" or start == "L" or start == "kL" or start == "ML":
                return(start)
                break
            else:
                print(option_error)


# Asks for ending unit
def end_unit():

    while True:
        
        # Asks for ending unit for distance
        if type == "distance":
            end = str(input('Please enter your starting unit of measurement, "mm", "cm", "m", or "km": '))
            # Checks for invalid answers
            if end == "mm" or end == "cm" or end == "m" or end == "km":
                return(end)
                break
            else:
                print(option_error)

        # Asks for ending unit for mass
        elif type == "mass":
            end = str(input('Please enter your starting unit of measurement, "mg", "g", "kg", or "t": '))
            # Checks for invalid answers
            if end == "mg" or end == "g" or end == "kg" or end == "t":
                return(end)
                break
            else:
                print(option_error)

        # Asks for ending unit for time
        elif type == "time":
            end = str(input('Please enter your starting unit of measurement, "ms", "sec", "min", "hr", "day", "wk", "mth", or "yr": '))
            # Checks for invalid answers
            if end == "ms" or end == "sec" or end == "min" or end == "hr" or end == "day" or end == "wk" or end == "mth" or end == "yr":
                return(end)
                break
            else:
                print(option_error)

        # Asks for ending unit for volume
        elif type == "volume":
            end = str(input('Please enter your starting unit of measurement, "mL", "L", "kL", or "ML": '))
            # Checks for invalid answers
            if end == "mL" or end == "L" or end == "kL" or end == "ML":
                return(end)
                break
            else:
                print(option_error)


# Doing the conversions
def convert(amount, start, end):

    # Conversions for distance
    if type == "distance":
        # Starting at mm
        if start == "mm":
            if end == "mm":
                output = amount
            elif end == "cm":
                output = amount / 10
            elif end == "m":
                output = amount / 1000
            elif end == "km":
                output = amount / 1000
        
        # Starting at cm
        elif start == "cm":
            if end == "mm":
                output = amount * 10
            elif end == "cm":
                output = amount
            elif end == "m":
                output = amount / 100
            elif end == "km":
                output = amount / 100000

        # Starting at m
        elif start == "m":
            if end == "mm":
                output = amount * 1000
            elif end == "cm":
                output = amount * 100
            elif end == "m":
                output = amount
            elif end == "km":
                output = amount / 1000
        
        # Starting at km
        elif start == "km":
            if end == "mm":
                output = amount * 1000000
            elif end == "cm":
                output = amount * 100000
            elif end == "m":
                output = amount * 1000
            elif end == "km":
                output = amount


    # Conversions for mass
    elif type == "mass":
        # Starting at mg
        if start == "mg":
            if end == "mg":
                output = amount
            elif end == "g":
                output = amount / 1000
            elif end == "kg":
                output = amount / 1000000
            elif end == "t":
                output = amount / 1000000000
        
        # Starting at g
        elif start == "g":
            if end == "mg":
                output = amount * 1000
            elif end == "g":
                output = amount
            elif end == "kg":
                output = amount / 1000
            elif end == "t":
                output = amount / 1000000

        # Starting at kg
        elif start == "kg":
            if end == "mg":
                output = amount * 1000000
            elif end == "g":
                output = amount * 1000
            elif end == "kg":
                output = amount
            elif end == "t":
                output = amount / 1000
        
        # Starting at t
        elif start == "t":
            if end == "mg":
                output = amount * 1000000000
            elif end == "g":
                output = amount * 1000000
            elif end == "kg":
                output = amount * 1000
            elif end == "t":
                output = amount


    # Conversions for time
    elif type == "time":
        # Starting at ms
        if start == "ms":
            if end == "ms":
                output = amount
            elif end == "sec":
                output = amount / 1000
            elif end == "min":
                output = amount / 60000
            elif end == "hr":
                output = amount / 3600000
            elif end == "day":
                output = amount / 86400000
            elif end == "wk":
                output = amount / 604800000
            elif end == "mth":
                output = amount / 2419200000
            elif end == "yr":
                output = amount / 29030400000
        
        # Starting at sec
        elif start == "sec":
            if end == "ms":
                output = amount * 1000
            elif end == "sec":
                output = amount
            elif end == "min":
                output = amount / 60
            elif end == "hr":
                output = amount / 3600
            elif end == "day":
                output = amount / 86400
            elif end == "wk":
                output = amount / 604800
            elif end == "mth":
                output = amount / 2419200
            elif end == "yr":
                output = amount / 29030400

        # Starting at min
        elif start == "min":
            if end == "ms":
                output = amount * 60000
            elif end == "sec":
                output = amount * 60
            elif end == "min":
                output = amount
            elif end == "hr":
                output = amount / 60
            elif end == "day":
                output = amount / 1440
            elif end == "wk":
                output = amount / 10080
            elif end == "mth":
                output = amount / 40320
            elif end == "yr":
                output = amount / 483840

        # Starting at hr
        elif start == "hr":
            if end == "ms":
                output = amount * 3600000
            elif end == "sec":
                output = amount * 3600
            elif end == "min":
                output = amount * 60
            elif end == "hr":
                output = amount
            elif end == "day":
                output = amount / 24
            elif end == "wk":
                output = amount / 168
            elif end == "mth":
                output = amount / 672
            elif end == "yr":
                output = amount / 8064

        # Starting at day
        elif start == "day":
            if end == "ms":
                output = amount * 86400000
            elif end == "sec":
                output = amount * 86400
            elif end == "min":
                output = amount * 1440
            elif end == "hr":
                output = amount * 24
            elif end == "day":
                output = amount 
            elif end == "wk":
                output = amount / 7
            elif end == "mth":
                output = amount / 28
            elif end == "yr":
                output = amount / 365.25

        # Starting at wk
        elif start == "wk":
            if end == "ms":
                output = amount * 604800000
            elif end == "sec":
                output = amount * 604800
            elif end == "min":
                output = amount * 10080
            elif end == "hr":
                output = amount * 168
            elif end == "day":
                output = amount * 7
            elif end == "wk":
                output = amount 
            elif end == "mth":
                output = amount / 4
            elif end == "yr":
                output = amount / 52

        # Starting at mth
        elif start == "mth":
            if end == "ms":
                output = amount * 2419200000
            elif end == "sec":
                output = amount * 2419200
            elif end == "min":
                output = amount * 40320
            elif end == "hr":
                output = amount * 672
            elif end == "day":
                output = amount * 28
            elif end == "wk":
                output = amount * 4
            elif end == "mth":
                output = amount 
            elif end == "yr":
                output = amount / 12

        # Starting at yr
        elif start == "yr":
            if end == "ms":
                output = amount * 31449600000
            elif end == "sec":
                output = amount * 31449600
            elif end == "min":
                output = amount * 524160
            elif end == "hr":
                output = amount * 8736
            elif end == "day":
                output = amount * 365.25
            elif end == "wk":
                output = amount * 52
            elif end == "mth":
                output = amount * 12
            elif end == "yr":
                output = amount

    # Conversions for volume
    elif type == "volume":
        # Starting at mL
        if start == "mL":
            if end == "mL":
                output = amount
            elif end == "L":
                output = amount / 1000
            elif end == "kL":
                output = amount / 1000000
            elif end == "ML":
                output = amount / 1000000000

        # Starting at L
        elif start == "L":
            if end == "mL":
                output = amount * 1000
            elif end == "L":
                output = amount
            elif end == "kL":
                output = amount / 1000
            elif end == "ML":
                output = amount / 1000000

        # Starting at kL
        elif start == "kL":
            if end == "mL":
                output = amount * 1000000
            elif end == "L":
                output = amount * 1000
            elif end == "kL":
                output = amount
            elif end == "ML":
                output = amount / 1000

        # Starting at ML
        elif start == "ML":
            if end == "mL":
                output = amount * 1000000000
            elif end == "L":
                output = amount * 1000000
            elif end == "kL":
                output = amount * 1000
            elif end == "ML":
                output = amount



    return(output)

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
    # Asks to continue program after instructions
    input("\nPress <enter> to continue. ")

else:
    print()

# Runs the conversion calculator
keep_going = ""

# Loops code
while keep_going == "":

    # Runs the input questions
    type = conversion_type()
    amount = ask_amount()
    startt = start_unit()
    endd = end_unit()

    # Converts the measurement and prints output
    outputt = convert(amount, startt, endd)
    print(f"\n{amount}{startt} converted to {endd}, is {outputt}{endd}. ")

    # Asks whether wants to repeat program or not
    keep_going = input("\nWould you like to do another conversion? If yes, press <enter>, if no, press any other key. ")
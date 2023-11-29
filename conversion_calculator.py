# Number Conversion Calculator by  
# The program is a command-line number converter, allowing users to convert between binary, decimal, hexadecimal, and octal numbers.
# Provides a user-friendly interface and input validation.
# Continues running until the user chooses to stop converting numbers, and the program terminates.

# Function to convert binary to decimal
from os import system, name

def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def binary_to_decimal(binary_str):
    decimal_num = 0
    power = len(binary_str) - 1

    # Iterate through each digit in the binary string
    for digit in binary_str:
        # If the digit is '1', add 2 to the power of the current position to the decimal number
        if digit == '1':
            decimal_num += 2 ** power
        power -= 1

    # Return the final decimal number
    return decimal_num

# Function to convert decimal to binary
def decimal_to_binary(decimal_num):
    binary_str = ""

    # Loop until the decimal number is greater than 0
    while decimal_num > 0:
        # Get the remainder when dividing the decimal number by 2
        remainder = decimal_num % 2
        # Prepend the remainder to the binary string
        binary_str = str(remainder) + binary_str
        # Update the decimal number by performing integer division by 2
        decimal_num //= 2

    # Return the final binary string or "0" if empty
    return binary_str if binary_str else "0"

# Function to convert binary to hexadecimal
def binary_to_hex(binary_str):
    # Convert binary to decimal and then decimal to hexadecimal
    decimal_num = binary_to_decimal(binary_str)
    hex_str = decimal_to_hex(decimal_num)
    return hex_str

# Function to convert decimal to hexadecimal
def decimal_to_hex(decimal_num):
    # Use the hex function to convert the decimal number to hexadecimal and remove the '0x' prefix
    hex_str = hex(decimal_num)[2:]
    # Convert the result to uppercase and return the final hexadecimal string
    return hex_str.upper()

# Function to convert hexadecimal to decimal
def hex_to_decimal(hex_str):
    # Use the int function to convert the hexadecimal string to decimal
    decimal_num = int(hex_str, 16)
    # Return the final decimal number
    return decimal_num

# Function to convert hexadecimal to binary
def hex_to_binary(hex_str):
    # Convert hexadecimal to decimal and then decimal to binary
    decimal_num = hex_to_decimal(hex_str)
    binary_str = decimal_to_binary(decimal_num)
    return binary_str

# Function to convert octal to decimal
def octal_to_decimal(octal_str):
    # Use the int function to convert the octal string to decimal
    decimal_num = int(octal_str, 8)
    # Return the final decimal number
    return decimal_num

# Function to convert decimal to octal
def decimal_to_octal(decimal_num):
    # Use the oct function to convert the decimal number to octal and remove the '0o' prefix
    octal_str = oct(decimal_num)[2:]
    # Return the final octal string
    return octal_str

# Main program loop
while True:
    # Clear the screen when the user continues converting numbers
    clear_screen()
    print("Welcome to my number converter! :333")
    print("Choose the following conversion:")
    print()
    print("(1) Binary to Decimal")
    print("(2) Decimal to Binary")
    print("(3) Binary to Hexadecimal")
    print("(4) Decimal to Hexadecimal")
    print("(5) Hexadecimal to Decimal")
    print("(6) Hexadecimal to Binary")
    print("(7) Octal to Decimal")
    print("(8) Decimal to Octal")
    selection = input("Enter a valid selection (1-8): ")

    # Binary to Decimal conversion
    if selection == '1':
        binary_input = input("Enter a binary number: ")
        # Check if the input contains only '0' and '1'
        if all(digit in '01' for digit in binary_input):
            decimal_result = binary_to_decimal(binary_input)
            print("The number you converted is " + binary_input + ", this in decimal is " + str(decimal_result))
        else:
            print("Invalid binary input!")

    # Decimal to Binary conversion
    elif selection == '2':
        decimal_input = input("Enter a decimal number: ")
        # Check if the input consists of digits
        if decimal_input.isdigit():
            decimal_input = int(decimal_input)
            binary_result = decimal_to_binary(decimal_input)
            print("The number you converted is " + str(decimal_input) + ", this in binary is " + binary_result)
        else:
            print("Invalid decimal input!")

    # Binary to Hexadecimal conversion
    elif selection == '3':
        binary_input = input("Enter a binary number: ")
        # Check if the input contains only '0' and '1'
        if all(digit in '01' for digit in binary_input):
            hex_result = binary_to_hex(binary_input)
            print("The number you converted is " + binary_input + ", this in hexadecimal is " + hex_result)
        else:
            print("Invalid binary input!")

    # Decimal to Hexadecimal conversion
    elif selection == '4':
        decimal_input = input("Enter a decimal number: ")
        # Check if the input consists of digits
        if decimal_input.isdigit():
            decimal_input = int(decimal_input)
            hex_result = decimal_to_hex(decimal_input)
            print("The number you converted is " + str(decimal_input) + ", this in hexadecimal is " + hex_result)
        else:
            print("Invalid decimal input!")

    # Hexadecimal to Decimal conversion
    elif selection == '5':
        hex_input = input("Enter a hexadecimal number: ")
        # Check if the input contains valid hexadecimal characters
        if all(digit in '0123456789ABCDEFabcdef' for digit in hex_input):
            decimal_result = hex_to_decimal(hex_input)
            print("The number you converted is " + hex_input + ", this in decimal is " + str(decimal_result))
        else:
            print("Invalid hexadecimal input!")

    # Hexadecimal to Binary conversion
    elif selection == '6':
        hex_input = input("Enter a hexadecimal number: ")
        # Check if the input contains valid hexadecimal characters
        if all(digit in '0123456789ABCDEFabcdef' for digit in hex_input):
            binary_result = hex_to_binary(hex_input)
            print("The number you converted is " + hex_input + ", this in binary is " + binary_result)
        else:
            print("Invalid hexadecimal input!")

    # Octal to Decimal conversion
    elif selection == '7':
        octal_input = input("Enter an octal number: ")
        # Check if the input contains valid octal characters
        if all(digit in '01234567' for digit in octal_input):
            decimal_result = octal_to_decimal(octal_input)
            print("The number you converted is " + octal_input + ", this in decimal is " + str(decimal_result))
        else:
            print("Invalid octal input!")

    # Decimal to Octal conversion
    elif selection == '8':
        decimal_input = input("Enter a decimal number: ")
        # Check if the input consists of digits
        if decimal_input.isdigit():
            decimal_input = int(decimal_input)
            octal_result = decimal_to_octal(decimal_input)
            print("The number you converted is " + str(decimal_input) + ", this in octal is " + octal_result)
        else:
            print("Invalid decimal input!")

    else:
        print("Invalid selection!")

    # Ask the user if they want to perform another conversion
    try_again = input("Do you want to perform another conversion? (yes/no): ")
    if try_again.lower() != 'yes':
        break

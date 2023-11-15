Var = 42

def add(num1, num2, current_var):
    return num1 + num2 + current_var

def main():
    global Var
    while True:
        try:
            user_input1 = int(input("Enter the first number: "))
            user_input2 = int(input("Enter the second number: "))
            number = add(user_input1, user_input2, Var)
            print("Sum:", number, "is a whole number.")
            
            Var = user_input1 + user_input2

            user_choice = input("Do you want to add more numbers? (Y/N): ").upper()
            if user_choice != "Y":
                break

        except ValueError:
            print("Invalid input. Please enter valid numbers and try again.")

if __name__ == "__main__":
    main()

# Function to handle user selection
def user_selection(num):
    print("User selected:" + num)

# Main program
def main():
    # Infinite loop until the user decides to quit
    while True:
        # Prompt the user for input
        user_input = input("Enter a number (or 'q' to quit): ")
        
        # Check if the user wants to quit
        if user_input.lower() == 'q':
            print("Quitting the program.")
            break  # Exit the loop if 'q' is entered
        
        try:
            # Convert user input to an integer
            num = int(user_input)
            
            # Call the function to handle the user's selection
            user_selection(num)
        except ValueError:
            # Handle the case where the input is not a valid integer
            print("Invalid input. Please enter a valid number or 'q' to quit.")

# Run the main function if the script is executed
if __name__ == "__main__":
    main()

# Example of Stack Overflow

def stack_me_high(num1):
    if num1 == 0:
        return num1
    print("Current count: ", num1)
    # Returns the current counted number with "Current count:"
    num1 += 1
    # Repeatedly adds 1 to the current number and prints it.
    stack_me_high(num1)
    # Process will continue until it reaches the stack limit, where it will crash causing a stack overflow.

def main():
    num1 = stack_me_high(1)
    print("Current count: ", num1)

if __name__ == "__main__":
    main()
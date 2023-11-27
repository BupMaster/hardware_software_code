def while_counter(num):
    while num > 0:
        print(num)
        num -= 1

def for_counter(num):
    for i in range(num, 0, -1):
        print(i)

def main():
    counter = 10
    print("Counting down using while loop:")
    while_counter(counter)

    print("\nCounting down using for loop:")
    for_counter(counter)

if __name__ == "__main__":
    main()

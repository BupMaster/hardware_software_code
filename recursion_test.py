def stack_me(num1):
    if num1 == 0 | num1 == 10:
        print("add stack_me: ", num1)
        print("finished: ")
        return num1
    print("add stack_me: ", num1)
    num1 += 1
    return_me = stack_me(num1)
    print("remove stack_me: ", num1, end=" ")
    print("return_me", num1)

def main():
    start = 1
    num1 = stack_me(start)
    print("Back in Main", end=" ")
    print("remove stack_me", num1)

if __name__ == "__main__":
    main()
def meal_test(answer):
    if answer == 1:
        return "Fried Chicken Yummy!"
    elif answer == 2:
        return "Hamburger Yummy!"
    elif answer == 3:
        return "Pizza Yummy!"
    else:
        return "That is not an option!"

def main():
    print("Which is your favorite meal?")
    print("1: Fried Chicken")
    print("2: Hamburger")
    print("3: Pizza")
    answer = int(input())
    result = meal_test(answer)
    print(result)

if __name__ == "__main__":
    main()

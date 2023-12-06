def main():
    animals = {
        1: "Cats",
        2: "Dogs",
        3: "Birds",
        4: "Fish",
        5: "Rabbits",
    }

    print("Animal List:")
    for key, value in animals.items():
        print("{}. {}".format(key, value))

    user_choice = int(input("Pick a number to choose your favorite animal: "))

    if user_choice in animals:
        chosen_animal = animals[user_choice]
        print("You chose {} as your favorite animal!".format(chosen_animal))
    else:
        print("Invalid choice. Please pick a number from the menu.")

if __name__ == "__main__":
    main()

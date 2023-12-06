from os import system, name

def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def display_menu(menu_dict):
    # Displays the menu items with their corresponding numbers.
    for items, values in menu_dict.items():
        print(items + ". " + values.capitalize())

def add_fruit(menu_dict, next_key):
    # Allows the user to add their favorite fruit to the menu.
    user_fruit = input("Enter the name of your favorite fruit: ")
    
    # Assigning the next available key
    user_key = str(next_key)
    menu_dict[user_key] = user_fruit

    # Increment the next key for the next addition
    next_key += 1

    # Clear the screen and then display the message
    clear_screen()
    print("Great choice! '{}' has been added to the menu.".format(user_fruit.capitalize()))
    print()

def main():
    # Main function to run the menu program.
    menu_dict = {
        '1': 'apples',
        '2': 'bananas',
        '3': 'cherries',
        'X': 'pick your own',
    }

    next_key = len(menu_dict) + 1

    while True:
        display_menu(menu_dict)

        print()
        user_choice = input("Enter the number of your favorite fruit or 'X' to add your own (Q to quit): ").upper()

        if user_choice == 'Q':
            break
        elif user_choice == 'X':
            add_fruit(menu_dict, next_key)
        elif user_choice in menu_dict:
            print("You chose: {}, nice choice!".format(menu_dict[user_choice].capitalize()))
            print()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

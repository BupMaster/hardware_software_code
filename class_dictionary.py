def display_menu():
    menu_dict = {
        '1': 'Apples',
        '2': 'Pears',
        '3': 'Bananas',
    }
    for item, values in menu_dict.items():
        print(item + ". " + values)

def main():
    display_menu()

main()

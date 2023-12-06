<<<<<<< HEAD
def display_menu(num):
    menu_dict = {
        '1' : 'Apples',
        '2' : 'Pears',
        '3' : 'Bananas',
    }
    for items, values in menu_dict() .items():
        print(items+". "+ values)

def main():
    display_menu()
=======
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
>>>>>>> refs/remotes/origin/main

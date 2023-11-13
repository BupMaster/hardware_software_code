def check_number():
    number = input("Enter a whole number: ")
    try:
        return(True, int(number))
    except:
        print("Invalid input!!")
        return(False, None)
    
def main():
    good_selection = False
    while not good_selection:
        good_selection, number = check_number()
    print("Good job,", number , "is a whole number!")

if __name__ == "__main__":
     main() 
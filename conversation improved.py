def conversation():
    print("Welcome to my conversation")
    print("Do you like coding?")

    answer = input("Answer yes or no: ")
    if answer in ["Yes", "yes"]:
        print("That's good!")
    elif answer in ["no","No"]:
        print("That's a shame!")
    else:
        print("I need a yes or no answer, sorry!")
    print("Thanks for talking with me!")

def main():
      conversation()

if __name__ == "__main__":
     main() 
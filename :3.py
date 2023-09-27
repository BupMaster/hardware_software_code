print( "We want to know if you like programmming!")
print()
name = input( "Please enter your name: ")
answer = input("Hi " + name + "!" + " Do you like programming? ")
if answer in ["yes","Yes"]:
    print( "Great! You said " + answer + "!" )
elif answer in ["no","No"]:
    print("What a shame! You said " + answer + "...")
print()
age = input("How old are you? ")
print( "Nice! You're " + age + " years old!")
print()
day = input("Are you having a good day today? Please respond with Yes or No: ")
if day in ["yes","Yes"]:
    print("That's great to hear!")
elif day in ["no","No"]:
    print("Oh no! Sorry to hear that.")
else:
    print("I don't seem to understand, I hope your day is going well!")
print()
color =input("What's your favorite color? ")
if color in ["Purple","Purple"]:
    print("Woah! Purple is my favorie color too!")
else:
    print("You said " + color + ". Nice choice!")
print()
print( "Let's learn some Python today!" )
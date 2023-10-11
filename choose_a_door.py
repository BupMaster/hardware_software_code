def choose_a_door():
    prize = 4
    message = "Choose the correct door, 1, 2, or 3: "
    print("Do you want to win a prize?")
    door = int(input(message))

    while door < 1 or door > 3:
        print("Invalid door!")
        door = int(input(message))
    if door == 1:
        prize = 2 + 9 // 10 * 100
    elif door == 2:
        prize += 6
    if door == 3:
        for i in range(door):
            prize += i
    print("You won", str(prize), "tickets!")
    
def main():
      choose_a_door()

if __name__ == "__main__":
     main() 
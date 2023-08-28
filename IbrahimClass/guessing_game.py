import random

my_number = random.randint(1,10)
counter = 0
def game() -> None:
    global my_number, counter

    if counter == 5:
        print("\nYou have tried five time, GoodLuck next time")
        exit()

    user_number = int(input("Enter your guess from 1 to 10 (You have 5 trials): "))
    counter += 1

    if user_number < my_number:
        print(f"Too low, try again, You have {5 - counter} trials left")
        game()
    elif user_number > my_number:
        print(f"Too high, try again, You have {5 - counter} trials left")
        game()
    elif user_number == my_number:
        print("Correct, You have guessed the number")


if __name__ == '__main__':
    game()
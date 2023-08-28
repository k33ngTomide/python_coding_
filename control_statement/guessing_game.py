import random
number = random.randint(0, 10)

counter = 0
while counter <= 10:
    user_guess = int(input("Enter a digit number guess:  "))

    if user_guess == number :
        print("Congratulations, you just WON a $3,000")
        break
    else:
        print(" Try again!")
    counter = counter + 1
    if counter == 10:
        print("Opps!! GAME OVER. You were not correct, try again!")
        exit()
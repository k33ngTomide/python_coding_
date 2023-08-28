

def roller_coaster():
    user_height = float(input("What is your height:  "))

    if user_height >= 6:
        age = int(input("Enter your age:  "))
        if age < 12:
            print("Price for your ride is N100")
        elif 12 <= age <= 60:
            print("Price for your ride is N200")
        else:
            print("Congratulations, we are offering a charity for Old People.\nYour ride is free!")
    else:
        print("People with height less than 5.9 are not allowed to ride.")


if __name__ == '__main__':
    roller_coaster()
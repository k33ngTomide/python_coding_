user_number = int(input("Enter a number between 0 and 1000:  "))

if 0 < user_number <= 1000:
    first_digit = (user_number// 1000)
    second_digit = (user_number// 100) % 10
    third_digit = (user_number// 10) % 10
    last_digit = user_number % 10

    print(first_digit, "\t", second_digit, "\t", third_digit, "\t", last_digit, "\n")

    total = first_digit + second_digit + third_digit + last_digit
    print("The sum of the digits is: ", total)
else:
    print("The number you entered is not within the given range")
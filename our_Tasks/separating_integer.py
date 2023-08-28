
user_number = int(input("Enter a five digit number: "))

if 9999 < user_number < 100000:
    first_digit = user_number // 10000
    second_digit = (user_number // 1000) % 10
    third_digit = (user_number // 100) % 10
    fourth_digit = (user_number // 10) % 10
    last_digit = user_number % 10

    print(first_digit, "\t", second_digit, "\t", third_digit, "\t", fourth_digit, "\t", last_digit)
else:
    System.out.println("The number you entered is not a Five digit number")
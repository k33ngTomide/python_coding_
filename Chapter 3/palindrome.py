user_input = int(input('Enter a five digit number: '))

digit_one = user_input // 10000
digit_two = user_input // 1000 % 10
digit_three = user_input // 100 % 10
digit_four = user_input // 10 % 10
digit_five = user_input % 10

if digit_five == digit_one and digit_four == digit_two:
    print('The number you entered is a Palindrome')
else:
    print('The number you entered is not a Palindrome')
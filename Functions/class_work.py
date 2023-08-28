def check_even():
    user_entry = int(input("Enter a number:  "))
    if user_entry % 2 == 0:
        print('true')
    else:
        print('false')


check_even()


def check_even(user_entry):
    if user_entry % 2 == 0:
        print('true')
    else:
        print('false')


check_even(45)
check_even(43)
check_even(48)


def print_fizz_buzz():

    for number in range(1, 50):
        if number % 5 == 0 and number % 3 == 0:
            print("FizzBuzz")
        elif number % 5 == 0:
            print("Buzz")
        elif number % 3 == 0:
            print("Fizz")
        else:
            print(number)

if __name__ == '__main__':
    print_fizz_buzz()
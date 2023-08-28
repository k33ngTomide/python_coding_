

def get_common_divisor(num1, num2):

    divisor = 0
    for counter in range(2, num1):
        if (num1 % counter == 0) and (num2 % counter == 0):
            divisor = counter
    if divisor == 0:
        divisor = None
    return f'The divisor is: {divisor}'

if __name__ == '__main__':

    first_number = int(input("Enter first number"))
    second_number = int(input("Enter second number"))

    print(get_common_divisor(first_number, second_number))
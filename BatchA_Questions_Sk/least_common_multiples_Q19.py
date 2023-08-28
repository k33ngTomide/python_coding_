

def get_common_multiples(num1, num2):

    multiples = 0
    for counter in range(num1*num2 + 1):
        if counter % num1 == 0 and counter % num2 == 0:
            multiples = counter

    if multiples == 0:
        multiples = None
    return f'The divisor is: {multiples}'

if __name__ == '__main__':

    first_number = int(input("Enter first number"))
    second_number = int(input("Enter second number"))

    print(get_common_multiples(first_number, second_number))
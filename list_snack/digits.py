

def main():
    user_entry = "243536"
    print(digit_of_input(user_entry))


def digit_of_input(numbers: int) -> list:
    new_list = []
    for number in range(len(numbers)):
       x = numbers[number]

       new_list += x
    return new_list


if __name__ == '__main__':
    main()
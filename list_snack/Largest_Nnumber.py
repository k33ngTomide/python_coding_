
def largest(number: list) -> int:
    largest_number = number[0]

    for value in number:
        if value > largest_number:
            largest_number = value

    return largest_number


if __name__ == '__main__':
    largest_number = largest([2, 4, 56, 32, 23, 6])
    print("The largest Number is:", largest_number)
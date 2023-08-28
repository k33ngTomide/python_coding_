
def largest_odd_number(numbers: list):

    odd_list = [numbers for numbers in numbers if numbers % 2 != 0]

    biggest_odd_number = odd_list[0]
    for number in odd_list:
        if number > biggest_odd_number:
            biggest_odd_number = number

    return biggest_odd_number


if __name__ == '__main__':
    largest = largest_odd_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    print("The largest odd number is: ",largest)


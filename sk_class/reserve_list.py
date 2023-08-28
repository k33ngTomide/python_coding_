
def reverse_list(num: list) -> list:

    new_list = []
    for counter in range(len(num)):
        x = num[-1 - counter]
        new_list += [x]
    return new_list


if __name__ == '__main__':
    number = [8, 2, 5, 6, 1, 3, 9, 4, 7]
    print(reverse_list(number))
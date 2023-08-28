
def sorted_list(num: list) -> list:
    for counter in range(len(num)):
        for new_counter in range(len(num)):
            if num[new_counter] > num[counter]:
                num[new_counter], num[counter] = num[counter], num[new_counter]
    return num


if __name__ == '__main__':
    number = [8, 2, 5, 6, 1, 3, 9, 4, 7]
    print(sorted_list(number))
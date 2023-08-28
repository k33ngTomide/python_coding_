
def main() -> None:
    number = [2, 3, 6, 7, 8, 10, 11, 13, 15, 16]
    print(odd_indexes(number))


def odd_indexes(array_list: list) -> list:
    new_array = []

    for counter in range(len(array_list)) :
        if counter % 2 == 0:
            new_array.append(array_list[counter])

    return new_array

if __name__ == '__main__':
    main()
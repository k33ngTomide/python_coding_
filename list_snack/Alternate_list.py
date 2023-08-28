
def main() -> None:
    first_list = ['a', 'b', 'c']
    second_list = [1, 2, 3]

    print(alternate_list(first_list, second_list))


def alternate_list(character:list, number:list) -> list:
    new_list = []
    new_counter = 0
    extra_counter = 0
    for counter in range(len(number) + len(character)):

        if counter % 2 == 0:
            new_list.append(character[new_counter])
            new_counter += 1
        else:
            new_list.append(number[extra_counter])
            extra_counter += 1

    return new_list

if __name__ == '__main__':
    main()
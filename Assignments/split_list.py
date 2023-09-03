def list_rearrange(data: list):
    first_list = [data[counter] for counter in range(0, len(data), 3)]
    second_list = [data[counter] for counter in range(1, len(data), 3)]
    third_list = [data[counter] for counter in range(2, len(data), 3)]

    return [first_list, second_list, third_list]


if __name__ == '__main__':
    list_of_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
    print(list_rearrange(list_of_letters))
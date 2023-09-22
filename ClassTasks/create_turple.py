
def create_tuple(first_list: list, second_list: list) -> list[tuple]:
    # return [
    #     (first_list[counter], second_list[counter]) for counter in range(len(first_list))
    # ]

    new_list = []
    if len(first_list) == len(second_list):
        new_list.extend(
            (first_list[counter], second_list[counter])
            for counter in range(len(first_list))
        )
        return new_list
    elif len(first_list) > len(second_list):
        new_list.extend(
            (first_list[counter], second_list[counter])
            for counter in range(len(second_list))
        )
        new_list.extend((number, ) for number in first_list[len(second_list)::])
        return new_list

    elif len(second_list) > len(first_list):
        new_list.extend(
            (first_list[counter], second_list[counter])
            for counter in range(len(first_list))
        )
        new_list.extend((number, ) for number in second_list[len(first_list)::])
        return new_list


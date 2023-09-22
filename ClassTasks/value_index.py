
def sum_list(list_of_numbers: list, value: int) -> list:

    # for counter in range(0, len(list_of_numbers)):
    #     for new_counter in range(1, len(list_of_numbers)):
    #         if list_of_numbers[counter] + list_of_numbers[new_counter] == value:
    #             return [counter, new_counter]

    for first in list_of_numbers[::]:
        for second in list_of_numbers[1::]:
            if second + first == value:
                return [list_of_numbers.index(first), list_of_numbers.index(second)]

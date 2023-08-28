def even_indexes(array_list: list) -> list:
    new_array = []

    for counter in range(len(array_list)) :
        if counter % 2 != 0:
            new_array.append(array_list[counter])

    return new_array


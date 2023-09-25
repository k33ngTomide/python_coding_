
def add(first_array :list, second_array: list) -> list:
    numbers = list(first_array[::-1])

    for space in second_array[::-1]:
        numbers.append(space)

    return numbers

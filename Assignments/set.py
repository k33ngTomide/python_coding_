

def intersection_finder(first_list: list, second_list: list) -> tuple:

    intersect_list = []

    for element in first_list:
        if element in second_list and element not in intersect_list:
            intersect_list += [element]
    return tuple(intersect_list)

# def list_union(first_list: list, second_list: list) -> list:
#
#     union_list = list(set(first_list))
#
#     for element in second_list:
#         if element not in union_list:
#             union_list += [element]
#     return sorted(union_list)


if __name__ == '__main__':
    list_one = [20, 30, 60, 65, 75, 90, 90, 80, 85]
    list_two = [42, 30 , 80, 90, 65, 68, 88, 95]

    print(intersection_finder(list_one, list_two))


def count_elements(data_list) -> list:
    new_list = []
    new_data_list = []

    for item in data_list:
        if item not in new_list: new_list += [item]

    for data in new_list:
        counted = data_list.count(data)
        new_data_list += [(data, counted)]

    return new_data_list

if __name__ == '__main__':
    user_list = ["male", "female", "female", "male", "male",
                 "female", "male", "male", "male", "female", "female", "male"]

    processed_list = count_elements(user_list)
    print(processed_list)
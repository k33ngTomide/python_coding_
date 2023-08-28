
def unique(data_list) :
    new_list = []

    for item in data_list:
        if item not in new_list: new_list += [item]

    return new_list

if __name__ == '__main__':
    unique_data = unique([34, 23, 24, 21, 33, 33, 24, 34, 23, 21])
    print(unique_data)

    checked_list = unique("AKARA")
    print(checked_list)


def check_presence(first_list, second_list):

    new_list = []
    for element in first_list:
        if element not in second_list:
            new_list += [element]
    return set(new_list)

if __name__ == '__main__':
    color_list_1 = {"white", "black", "red"}
    color_list_2 = {"red", "green"}

    print(check_presence(color_list_1, color_list_2))

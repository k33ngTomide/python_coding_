
def check(element, data_list):

    is_present = any(element == x for x in data_list)

    print(is_present)

if __name__ == '__main__':
    number = 3
    new_list = [1,5,8,3]
    check(number, new_list)
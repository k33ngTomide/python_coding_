
def concate(data_list):
    word = ""

    for element in data_list:
        word += element
    return word

if __name__ == '__main__':
    new_data = ["a", "k", "i", "n"]
    print(concate(new_data))
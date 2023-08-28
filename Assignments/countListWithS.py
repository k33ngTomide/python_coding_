
def s_counter(data_list: list[str]):

    output = {}
    new_data = [item.capitalize() for item in data_list]

    new_data_list = [item for item in new_data if item.startswith("S")]


    for data in new_data_list:
        elementNumber = new_data.count(data)
        output[data] = elementNumber

    return output

if __name__ == '__main__':
    names = ["joel", "Daniel", "Seyi", "Kelvin", "Muhammed", "Hakimi", "Segun", "Ashley", "seyi"]

    print(s_counter(names))
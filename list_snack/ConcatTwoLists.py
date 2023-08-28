

def main() -> None:
    first_list = ['a','b','c']
    second_list = [1, 2, 3]

    print(concatenate_lists(first_list, second_list))
def concatenate_lists(characters: list, number:list) -> list :
    new_list = []

    for element in characters:
        new_list.append(element)

    for element in number:
        new_list.append(element)



    return new_list;


if __name__ == '__main__':
    main()
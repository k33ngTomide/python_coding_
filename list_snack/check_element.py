
def main() -> None:
    search = 5
    numbers = [2, 3, 6, 5, 6, 7]
    is_present = check_list(search, numbers)
    print("is ", search, " in the list? ", is_present)

def check_list(find, array_list) -> bool:
    return find in array_list


if __name__ == '__main__':
    main()
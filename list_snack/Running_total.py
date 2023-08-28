
def main():
    new_list = [1, 2, 3, 4, 5]

    sum_of_array = total(new_list)
    print("The sum is: ", sum_of_array)

def total(array_list: list) -> int:
    total = 0

    for value in array_list:
        total = total + value

    return total

if __name__ == '__main__':
    main()
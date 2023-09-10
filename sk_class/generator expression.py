

def number_printer(numbers: int):
    new_list = [number for number in range(numbers) if number % 5 == 0]
    print(new_list)


if __name__ == '__main__':
    number_printer(100)

def get_sum_of_list_with_for(numbers: list) -> int:
    total = 0
    for number in numbers:
        total += number

    return total

def  get_sum_of_list_with_while(numbers: list) -> int:

    total = 0
    counter = 0

    while counter < len(numbers) :
        total += numbers[counter]
        counter+=1

    return total

def main() -> None:
    number = [34, 39, 38, 36]
    sum_with_while = get_sum_of_list_with_while(number)
    sum_with_for = get_sum_of_list_with_for(number)

    print("The sum with for-loop is: ", sum_with_for)
    print("The sum with while-loop is:", sum_with_while)

if __name__ == '__main__':
    main()
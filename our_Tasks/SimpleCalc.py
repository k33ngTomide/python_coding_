
def calculate() -> str:
    example = input(">>>")
    first_number = int(example[0])
    second_number = int(example[4])

    if example[2] == "+":
        answer_addition = first_number + second_number
        return str(answer_addition)

    elif example[2] == "-":
        answer_subtract = first_number - second_number
        return str(answer_subtract)

    elif example[2] == "*":
        answer_multiply = first_number * second_number
        return str(answer_multiply)
    invalid = "Invalid Operator"
    return invalid


def calc():
    print("Welcome to a Simple Calculator")
    print(calculate())


calc()

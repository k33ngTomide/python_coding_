
def calculator() -> str:
    number_1, operator, number_2 = input('').split(" ", 2)

    if operator == "+":
        answer_addition = int(number_1) + int(number_2)
        return str(answer_addition)

    elif operator == "-":
        answer_subtract = int(number_1) - int(number_2)
        return str(answer_subtract)

    elif operator == "*":
        answer_multiply = int(number_1) * int(number_2)
        return str(answer_multiply)

    invalid = "Invalid Operator"
    return invalid


def calca():
    print("Welcome to a Simple Calculator")
    print(calculator())


if __name__ == '__main__':
    calca()

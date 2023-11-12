# def divide(inputed: str):
#     first_number, second_number = inputed.split(" ")
#     try:
#         return int(first_number) / int(second_number)
#     except ZeroDivisionError as e:
#         raise ZeroDivisionError("integer division or modulo by zero") from e
#     except ValueError as e:
#         raise ValueError(
#             f"invalid literal for int() with base 10: \\'{second_number}\\' "
#         ) from e
#
#
# if __name__ == "__main__":
#
#     number = int(input())
#
#     for number in range(number):
#         try:
#             numbers = input()
#             output = divide(numbers)
#             print(output)
#         except ValueError as e:
#             print(f"Error Code: {e}")
#         except ZeroDivisionError as e:
#             print(f"Error Code: {e} ")


def divide(inputed):
    first_number, second_number = map(int, inputed.split())
    if second_number == 0:
        raise ZeroDivisionError("integer division or modulo by zero")
    return first_number // second_number


if __name__ == "__main__":
    try:
        num_tests = int(input())
        for _ in range(num_tests):
            try:
                numbers = input()
                output = divide(numbers)
                print(output)
            except (ValueError, ZeroDivisionError) as e:
                print(f"Error Code: {e}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

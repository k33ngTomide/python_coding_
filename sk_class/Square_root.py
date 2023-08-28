

def divide_or_square(number: int) -> float:
    return number ** 0.5 if number % 5 == 0 else number % 5


if __name__ == '__main__':
    print(f"{divide_or_square(10): .2f}")


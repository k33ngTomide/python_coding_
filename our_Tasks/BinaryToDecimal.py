
def to_decimal(binary: int ) -> int:

    total = 0
    for counter in range(len(str(binary))):
        digit = (binary // (10**counter)) % 10

        binary_individual = digit * (2**counter)
        total += binary_individual

    return total

def main() -> None:
    decimal_value = to_decimal(11011)

    print(decimal_value)


if __name__ == '__main__':
    main()
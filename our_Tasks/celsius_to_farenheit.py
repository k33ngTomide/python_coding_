
def main() -> None:
    celsius = int(input("Enter the temperature in celsius:  "))

    fahrenheit = (9.0 / 5) * celsius + 32
    print(celsius, " Celcius is ", fahrenheit, " Fahrenheit")


if __name__ == '__main__':
    main()

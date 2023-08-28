

def fibonacci(n: int) -> None:
    number = [0,1]

    for counter in range(2,n): number.append(number[counter-1]  + number[counter -2])

    for element in number:
        if element <= n:
            print(element, end=", ")


if __name__ == '__main__':
    fibonacci(100)
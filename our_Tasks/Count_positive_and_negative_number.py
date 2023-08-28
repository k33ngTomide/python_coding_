
total = 0.0
counter = 0
positive_counter = 0
negative_counter = 0

number = int(input("Enter an integer, the input ends if it is 0: "))

while number != 0:
    if number > 0:
        positive_counter += 1
    else:
        negative_counter += 1

    total += number
    counter += 1

    number = int(input("Enter an integer, the input ends if it is 0: "))

if counter == 0:
    System.out.println("No numbers are entered except 0")

if counter > 0:
    print(f"The number of positive is {positive_counter}")
    print(f"The number of Negative is {negative_counter}")
    print(f"The total is {total}")
    print(f"The average is {total / counter}")

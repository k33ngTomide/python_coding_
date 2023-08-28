

number = [10, 20, 30, 40, 50]

square_list = []

for counter in number:
    x = counter**2
    square_list += [x]

print(square_list)
largest = square_list[0]
smallest = square_list[0]

for counter in range(len(square_list)):
    if square_list[counter] > largest: largest = square_list[counter]
    if square_list[counter] < smallest: smallest = square_list[counter]

subtract_value = largest - smallest
print("The different is: ", subtract_value)
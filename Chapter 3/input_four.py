

user_input = int(input('Enter a number: '))

smallest = user_input
largest = user_input
total = user_input
product = user_input
counter = 1
for number in range(3):
    user_input = int(input('Enter a number: '))

    total += user_input
    product *= user_input
    counter += 1

    if user_input < smallest:
        smallest = user_input
    if user_input > largest:
        largest = user_input
average = total / counter

print(f'Sum = {total} \nAverage: {average} \nProduct: {product} \nNumber of Student: {counter} '
      f'\nSmallest Number: {smallest} \nLargest Number: {largest}')

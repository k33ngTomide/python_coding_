
largest = 0
second_largest = 0
for number in range(10):
    user = int(input('Enter a number:  '))

    if user > largest:
        largest = user
    if second_largest < user < largest:
        second_largest = user

print(f'The largest number is: {largest}'
      f'\nThe second largest number is: {second_largest}')


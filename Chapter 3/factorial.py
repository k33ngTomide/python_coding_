
user_entry = int(input('Enter the number: '))
factorial = 1
for x in range(user_entry, 1, -1):
    factorial *= x

print(f'{user_entry}! = {factorial}')
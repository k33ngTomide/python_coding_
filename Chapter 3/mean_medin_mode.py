
total = 0
counter = 0

user_entry = int(input("Enter a number: "))

while user_entry != -1:
    total += user_entry
    counter += 1

    user_entry = int(input("Enter a number or use -1 to get the answer:  "))

mean = total / counter
print(f'The mean is: {mean}')
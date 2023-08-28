binary = 0
user_entry = int(input("Enter a binary to convert to decimal: "))
user = user_entry
for x in range(len(str(user_entry))):
    digit = int(user_entry) % 10

    binary += digit * (2**x)
    user_entry = user_entry // 10

print(f'The decimal of {user} is {binary}')

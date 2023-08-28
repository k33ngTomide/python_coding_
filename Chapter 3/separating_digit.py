user_input = int(input('Enter a five digit number: '))

for a in range(5):
    digit = user_input % 10

    user_input = user_input // 10

    print(digit, end='\t')


balance, interest_rate = input("Enter the balance and the interest rate:").split(" ", 1)

balance = float(balance)
interest_rate = float(interest_rate)

interest = balance * (interest_rate / 1200)

print(f"The interest is {interest: .5f}")
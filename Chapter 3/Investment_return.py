amount_invested = int(input("Enter the original amount invested: $"))
rate = int(input("Enter the annual rate of return(%): "))
print("Year\t\tAmount of deposit($)")

for year in range(31):
    amount_of_deposit = amount_invested * ((1 + (rate/100))**year)

    print(f'{year}\t\t\t{amount_of_deposit}')
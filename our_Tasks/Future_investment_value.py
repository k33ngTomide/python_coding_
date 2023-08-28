
amount = float(input("Enter investment Amount: "))

annual_rate = float(input("Enter annual rate in percentage: "))

year = float(input("Enter the number of years: "))

monthly_rate = annual_rate/1200
future_value = amount* ((1 + monthly_rate)**(year*12))

print(f"Accumulated Value is {future_value: .4f} ")

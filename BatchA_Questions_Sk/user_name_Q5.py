
first_name, last_name = input("Enter your first name and last name: ").split(" ", 2)

first_name = first_name[::-1]
last_name = last_name[::-1]

print(f"{first_name} {last_name}")
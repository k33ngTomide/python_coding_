first_name = input("Enter your first name:  ")
if first_name == "" :
    print("Your first name cannot be empty, go and enter your name.")
    exit()
last_name = input("Enter your last name: ")
if last_name == "":
    print("Your last name cannot be empty, go and enter your name.")
    exit()

age = int(input("Enter your age:  "))
print("Your name is ", first_name, last_name, ". You age is ", age)
if age < 0:
    print("Your age cannot be a negative number: ")
    exit()
if 18 <= age < 65:
    print("Your age is ", age, "You are agile.")

if 0 <= age < 18:
    print("Your age is ", age, "You are an underage.")
    exit()

if age > 65:
    print("your age is ", age, "You are an Old citizen.")
    exit()


number = [10, 20, 30, 40, 50]
new_total_1 = 0
# for counter in number[1: :2]:
for counter in range(1, len(number), 2):
    new_total_1 = new_total_1 + number[counter]

print("The new total is: ", new_total_1)
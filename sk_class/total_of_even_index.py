
number = [10, 20, 30, 40, 50]

new_total = 0
# for counter in number[ : :2]:
for counter in range(0, len(number), 2):
    new_total = new_total + number[counter]

print("The total of even indexes is : ", new_total)
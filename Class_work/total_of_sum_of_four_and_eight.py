
total = 1
sum_total = 0
for counter in range(4, 5, +4):
    for new_counter in range(1, 6, 1):
        total*=counter
        sum_total += total
print(sum_total, end=" ")


total_1 = 1
sum_total_1 = 0
for counter in range(8, 10, +4):
    for new_counter in range(1, 6, 1):
        total_1 *= counter
        sum_total_1 += total_1
print(sum_total_1, end=" ")
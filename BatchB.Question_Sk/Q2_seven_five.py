

for counter in range(2701):
    if counter >= 1500 and counter % 7 == 0:
        for new_counter in range(1000):
            if 5 * new_counter == counter:
                print(counter, end="  ")
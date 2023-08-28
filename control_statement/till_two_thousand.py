if __name__ == "__main__":
    print(" ")
power = 0
total = 2 ** power

# while total <= 2000:
#
#     power += 1
#     total = 2 ** power
# print(total)

for x in range(0, 2000, 2 ** power):
    power += 1
print(total)
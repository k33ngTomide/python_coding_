y = "hi pycharm"
print("%15s" % y)

for x in range(1, 11):
    if x == 5:
        print(x, "is the number here.")
        continue
    if x == 7:
        print(x, "is the number here.")
        continue
    print("%6i  %8i" % (x, x))


for x in range(54):
    pass
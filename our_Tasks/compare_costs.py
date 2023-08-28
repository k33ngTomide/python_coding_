
packages = [0,0]

for counter in range(0, 2):
    weight, price = input("Enter weight and price for package:  ").split(" ", 1)

    weight = float(weight)
    price = float(price)

    thePackage = weight / price
    if thePackage > 0:
        packages[counter] = thePackage
    else:
        println("Invalid Input")

if packages[0] > packages[1]:
    print("Package 1 has better price")
else:
    print("Package 2 has better price")





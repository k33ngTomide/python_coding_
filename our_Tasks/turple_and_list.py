
tomide = (50, 70, 45, 86)
seyi = (75, 50, 50, 35)
joel = (40, 10, 77, 85)
eddie = (80, 70, 45, 55)
precious = (78, 77, 76, 75)
harry = (64, 65, 54, 49)
james = (60, 59, 47, 50)
laflare = (47, 65, 70, 75)
daniel = (45, 60, 75, 90)
sultan = (79, 55, 55, 60)

students = [["Tomide", 14, tomide],
            ["Seyi", 12, seyi],
            ["Joel", 15, joel],
            ["Eddie", 10, eddie],
            ["Moyin", 19, precious],
            ["Harry", 16, harry],
            ["James", 15, james],
            ["Laflare", 13, laflare],
            ["Daniel", 14, daniel],
            ["Sultan", 13, sultan]]

print("----------------------------------------")
print("%-20s %5s" % ("Student", "Score"))
print("---------------------------------------------------------------")
print("%-10s\t %10s" % ("Name \t\t Age","E \t M \t Y \t A"))
print("---------------------------------------------------------------")
for number in students:
    print('\t\t'.join(map(str, number)))

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

for row in picture:
    for p in row:
        if p == 0:
            print(" ", end= ' ')
        if p == 1:
            print("*", end= ' ')
    print()

a = 0
while a < 8:
    for x in range(len(picture[a])):
        if picture[a][x] == 0:
            picture[a][x] = " "
        if picture[a][x] == 1:
            picture[a][x] = "*"
    print(' '.join(map(str, picture[a])))
    a+=1




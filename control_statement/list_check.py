storm = [
    [0, 0, 2, 2, 2, 0, 0],
    [0, 2, 1, 1, 1, 2, 0],
    [2, 1, 1, 1, 1, 1, 2],
    [2, 1, 1, 2, 1, 1, 2],
    [2, 1, 1, 2, 1, 1, 2],
    [2, 1, 1, 1, 1, 1, 2],
    [0, 2, 1, 1, 1, 2, 0],
    [0, 0, 2, 2, 2, 0, 0]
]

for a in range(8):
    for x in range(len(storm[a])):
        if storm[a][x] == 2:
            storm[a][x] = "+"
        if storm[a][x] == 1:
            storm[a][x] = "."
        if storm[a][x] == 0:
            storm[a][x] = " "
    print(' '.join(map(str, storm[a])))



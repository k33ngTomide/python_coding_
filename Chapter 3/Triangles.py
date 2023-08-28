
for x in range(11):
    print()
    for y in range(x):
        print('*', end=' ')
print()

for x in range(10, 0, -1):
    print(' ')
    for y in range(x):
        print('*', end=' ')
print()

for x in range(11, 0, -1):
    print()
    for z in range(11-x):
        print(' ', end=' ')
    for g in range(0, x-1):
        print('*', end=' ')

for x in range(11):
    print()
    for z in range(11-x-1):
        print(' ', end=' ')
    for g in range(x):
        print('*', end=' ')



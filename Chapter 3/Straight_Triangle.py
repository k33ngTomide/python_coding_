def triangles(n):
    for x in range(n):
        for y in range(x + 1):
            print('*', end=' ')
        for u in range(n - x):
            print(' ', end=' ')
        for z in range(n - x):
            print('*', end=' ')
        for g in range(x):
            print(' ', end=' ')
        for k in range(x + 1):
            print(' ', end=' ')
        for z in range(n - x):
            print('*', end=' ')
        for a in range(n - x):
            print(' ', end=' ')
        for r in range(x + 1):
            print('*', end=' ')
        print()


triangles(10)

answer = 0
factorial = 1
e = 1
for value in range(1, 10):
    factorial *= value
    e += 1/factorial

print(e)

passes = 0
failures = 0
students = 1

result = int(input('Enter result (1= pass, 2 = fail):  '))
while students < 10:
    if result == 1:
        passes = passes + 1
    elif result == 2:
        failures = failures + 1
        result = int(input('Enter result (1= pass, 2 = fail):  '))
    students = students + 1

print('Passes: ', passes, '\nFailures: ', failures)
if passes > 8:
    print('Bonus for the instructor')
total_mile = 0
total_gallon = 0
gallon = float(input('Enter the gallons used (-1 to end): '))

while gallon != -1:
    total_gallon += gallon

    mile = float(input('Enter the miles driven: '))

    mile_per_gallon = mile / gallon
    print(f'The mile per gallon for this tank was: {mile_per_gallon}')

    total_mile += mile

    gallon = float(input('Enter the gallons used (-1 to end): '))
print(f'The Overall average mile per gallon is: {total_mile/total_gallon}')
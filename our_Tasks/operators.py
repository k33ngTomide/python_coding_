
number = int(input("Enter a number:  "))

andOperator = (number % 5==0) and (number % 6 == 0)
orOperator = (number % 5==0) or (number % 6 == 0)
exclusiveOperator = ((number % 5==0 ) ^ (number % 6 == 0))

print(f"Is {number} divisible by 5 and 6? {andOperator}" )
print(f"Is {number} divisible by 5 or 6? {orOperator}")
print(f"Is {number} divisible by 5 or 6, but not both? {exclusiveOperator}")
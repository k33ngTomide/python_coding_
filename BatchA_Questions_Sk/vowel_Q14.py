import string

vowel_4 = ['a', 'e', 'i', 'o', 'u']

letter = input("Enter a letter:  ")
letter = letter.lower()

if letter in vowel:
    print(f'{letter} is a vowel')
else:
    print(f"{letter} is not a vowel, it is a Consonant")
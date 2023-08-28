
def letter_print():
    word = input("Enter a Word: ")
    try:
        number = int(input("Enter a number: "))
        if len(word) < 2:
            print(f"{word}\n" * number)
        else:
            print(f"{word[0]} {word[1]}\n" * number)
    except ValueError:
        print("Only numbers are Accepted")


if __name__ == '__main__':
    letter_print()
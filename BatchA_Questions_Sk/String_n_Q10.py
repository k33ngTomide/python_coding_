
def repeated(data, n):

    if number > 0:
        print(f'{data} \n' * n)
    else:
        print("Invalid, try again")

if __name__ == '__main__':
    word = input("Enter a word: ")
    number = int(input("Enter the number of times you want it printed"))
    repeated(word, number)

def palindrome(word: str) -> bool:
    newWord = ""
    for counter in range(len(word)):
        character = word[(len(word) - 1) - counter]

        newWord = newWord + character

    return newWord.capitalize() == word.capitalize()



def palindrome(word: str) -> bool:
    return word == word[::-1]

if __name__ == '__main__':
    word = "Adebayo"
    isPalindrome = palindrome(word)

    print("is ", word, " a palindrome? ", isPalindrome)
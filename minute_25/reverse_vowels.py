

def reverse_vowels(word: str):
    vowels = ["a", "e", "i", "o", "u"]
    available_vowels = ""
    for letter in word:
        if letter.lower() in vowels:
            available_vowels += letter.lower()

    available_vowels = available_vowels[::-1]
    print(available_vowels)

    new_index = 0
    new_word = ""
    for index in range(len(word)):
        if word[index].lower() in vowels:
            new_word += available_vowels[new_index]
            new_index += 1
        else:
            new_word += word[index]

    return new_word


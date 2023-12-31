def is_equal_after_backspace(first_word: str, second_word: str):
    def impl_backspace(word) -> bool:
        new_word = ''
        for index in range(len(word)):
            if word[index] == '#':
                new_word = (word
                            .replace(word[index], "")
                            .replace(word[index - 1], ""))
            break

        if new_word.__contains__('#'):
            new_word = impl_backspace(new_word)

        return new_word

    first_word = impl_backspace(first_word)
    second_word = impl_backspace(second_word)

    return first_word == second_word


def impl_space_and_tab(given: str):
    return given.replace("&", " ").replace("%", ".    ")

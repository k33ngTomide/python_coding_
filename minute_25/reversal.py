def reverse_each(given: str):
    given = given.split(" ", 10)

    word = ""
    for counter in range(len(given)):
        given[counter] = given[counter][::-1]

        if counter == (len(given) - 1):
            word += given[counter]
        else:
            word += given[counter] + " "
    return word

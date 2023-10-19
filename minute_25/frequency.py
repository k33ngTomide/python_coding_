def get_most_frequent(given: list):

    frequency = 0
    count = 0
    most_frequent = 0

    for item in given:
        for item_ in given:
            if item == item_:
                count += 1

        if count > frequency:
            frequency = count
            most_frequent = item

    return most_frequent



# frequency = 0
# count = 0
# most_frequent = 0
#
# for counter in range(len(given)):
#     for newCounter in range(len(given)):
#         if given[counter] == given[newCounter]:
#             count += 1
#
#     if count > frequency:
#         frequency = count
#         most_frequent = given[counter]
#
# return most_frequent
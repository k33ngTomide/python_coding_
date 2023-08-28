# addition = 1200
# subtract = 189
#
#
# def start_function(number):
#     start_function =  2 * number
#
#     def start_():
#         global addition
#         addition += subtract + start_function
#         print("the addition is ", addition)
#
#     start_()
#     return start_function
#
#
# if __name__ == "__main__":
#     print(start_function(13))
#     print(start_function(45 + 10))
#     print(start_function(start_function(start_function(10))))

def bigger(number1, number2, number3, number4):
    all_number = [number1, number2, number3, number4]

    for x in range(len(all_number)):
        maxi = all_number[0]

        if all_number[x] > maxi:
            maxi = all_number[x]
    return maxi


def smallest(number1, number2, number3, number4):
    all_number = [number1, number2, number3, number4]

    for x in range(len(all_number)):
        mini = all_number[0]

        if all_number[x] < mini:
            mini = all_number[x]
    return mini


# def greater(number1, number2, number3, number4):
#     maximum = number1
#     if number2 > number1 and number2 > number3 and number2 > number4:
#         maximum = number2
#     if number3 > number2 and number3 > number4 and number3 > number1:
#         maximum = number3
#     if number4 > number3 and number4 > number2 and number4 > number1:
#         maximum = number4
#     return maximum


# def smaller(number1, number2, number3):
#     minimum = number1
#     if number2 < number1 and number2 < number3:
#         minimum = number2
#     elif number3 < number2 and number3 < number1:
#         minimum = number3
#     return minimum


if __name__ == "__main__":
    # print("The greatest number is ", greater(8, 2, 34, 10))
    # print("The smallest number is ", smaller(7, 5, 0))
    print(bigger(54, 65, 78, 32))
    print(smallest(43, 23, 49, 12))

# that = 1324
# this = "Aceclan"
#
# print(len(str(that)))
# print(len(this))
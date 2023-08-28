import re

type = ""
card_number = ""
validity_status = ""

def is_card_valid():
    if 13 <= len(card_number) <= 16:
        return  True
    return False

def card_type_detector(card_number: str):

    if is_card_valid():
        global type
        if card_number.startswith("4"): type += "Visa"
        elif card_number.startswith("5"): type += "MasterCard"
        elif card_number.startswith("37"): type += "America ExpressCard"
        elif card_number.startswith("6"): type += "Discover Card"
        else : type += "Invalid Card"

    else:
        type += "Invalid Card"

    return type

def card_validity_detector(card_number: str):

    global validity_status
    validity_status = "Invalid"

    if is_card_valid():
        even_total = 0
        odd_total = 0

        for counter in range(len(card_number)):

            if counter % 2 == 0:
                digit = int(card_number[counter])
                new_digit = digit * 2

                if new_digit >= 10: even_total += ((new_digit % 10) + (new_digit // 10))
                else: even_total += new_digit


            if counter % 2 != 0:
                digit = int(card_number[counter])
                odd_total += digit

        total_digits = even_total + odd_total
        if total_digits % 10 == 0: validity_status = "Valid"
        else: validity_status = "Invalid"

    return validity_status


def input_():
    global card_number

    user_card_number = input("Hello, Kindly enter card Details to verify: ")

    if re.search("^[0-9]+$",user_card_number):
        if 13 <= len(user_card_number) <= 16:
            card_number = user_card_number
            card_type_detector(user_card_number)
            card_validity_detector(user_card_number)

            print()
            print("*" * 40,
                    "\n**Credit Card Type: ", type,
                    "\n**Credit Card Number: ", user_card_number,
                    "\n**Credit Card Digit Length: ", len(user_card_number),
                    "\n**Credit Card Validity status: ", validity_status,
                    "\n", "*" * 40)
        else :
            print("Credit Card Number must be between 13 and 16")
            input_()
    else:
        print("Credit Card Number cannot be blank, contain letters or space. \nTry Again!")
        input_()

if __name__ == '__main__':
    input_()
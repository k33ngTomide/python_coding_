import datetime
import re

store_name = "STANDARD GROCERIES STORE"
branch = "MAIN BRANCH"
store_address = "497, C-WAY, LAGOS STATE, NIGERIA."
telephone = "+334228127223"
date = datetime.date.today()
customer_name = ""
cashier_name = ""
items_bought = []
item_price = []
item_pieces = []
discount = 0.0
sub_total = 0
customer_bill_total = 0
amount_paid = 0.0


def start_info_input():
    global customer_name
    user_input = input("What is the Customer's name? ")
    if re.fullmatch("^[A-Za-z\s]*$", user_input):
        customer_name = user_input
        item_name_input()
    else:
        print("This is not a valid name, Input a valid name")
        start_info_input()


def more_items():
    user_input = input("Add more Items?")

    is_yes = "yes"
    is_no = "no"

    if is_yes == user_input.lower():
        item_name_input()
    elif is_no == user_input.lower():
        cashier_info()
    else:
        print("Invalid Input, " +
              "\nEnter Yes (if there are more items) or " +
              "\nNo (if there is no more item)")
        more_items()


def cashier_info():
    global cashier_name
    user_input = input("What is your name?")
    if re.fullmatch("^[A-Za-z\s]*$", user_input):
        cashier_name = user_input
        discount_given()
    else:
        print("This is not a valid name, Input a valid name")
        cashierInfo()


def discount_given():
    global discount

    try:
        discount_g = float(input("How much discount will customer get?"))

        if 0 <= discount_g < 100:
            discount = discount_g
        else:
            raise ValueError
    except ValueError:
        print("Invalid discount, try again")
        discount_given()


def item_name_input():
    user_input = input("What did the user buy?")

    if re.fullmatch("^[A-Za-z\s]*$", user_input):
        items_bought.append(user_input)
        pieces_input()
    else:
        print("Input invalid")
        item_name_input()


def pieces_input():
    pieces = input("How many pieces")
    if re.search("^[0-9]+$", pieces):
        if int(pieces) > 0:
            item_pieces.append(int(pieces))
            price_input()
        else:
            print("Invalid Input, pieces can not be less than 0, try again")
            pieces_input()
    else:
        print("Invalid, input the number of pieces bought")
        pieces_input()


def price_input():

    try:
        product_price = float(input("How much per unit?"))

        if product_price <= 0:
            raise ValueError

        item_price.append(product_price)
        more_items()
    except ValueError:
        print("Invalid input, input the product price")
        price_input()


def bill_page():
    heading_info()
    double_design()
    header_printer()
    single_design()
    list_printing()
    single_design()
    sub_total_total()
    double_design()
    bill_total()
    double_design()
    print(f"THIS IS NOT A RECEIPT KINDLY PAY {customer_bill_total: .2f}")
    double_design()
    customer_pay()


def header_printer():
    print("\tITEM   ", "\t   QTY   ", "\tPRICE   ", "  \tTOTAL(NGN)  ")


def heading_info():
    global store_name, branch, store_address, telephone, cashier_name, date, customer_name
    print(f"\n{store_name} \n{branch}  \nLocation: {store_address} \nTEL: {telephone},"
          f"\nDate: {date} \nCashier: {cashier_name} \nCustomer name: {customer_name} ")


def list_printing():
    global sub_total
    for index in range(len(items_bought)):
        total = item_pieces[index] * item_price[index]
        sub_total += total
        print(f"{items_bought[index]: >10}  {item_pieces[index]: >10} {item_price[index]: >10} \t\t {total: >10}")


def restore():
    global sub_total
    sub_total = 0


def sub_total_total():
    print(f"Sub Total: {sub_total: >10.2f} \nDiscount:  {((discount / 100) * sub_total): >10.2f},"
          f"\nVAT @ 17.50%: {((sub_total / 100) * 17.5): >10.2f}")


def bill_total():
    global customer_bill_total

    bill = sub_total - ((discount / 100) * sub_total) + ((sub_total / 100) * 17.5)
    customer_bill_total = bill
    print(f"Bill Total:  {bill: >10.2f}")


def double_design():
    print("=" * 50)


def single_design():
    print("-" * 50)


def customer_pay():
    global amount_paid, customer_bill_total
    try:
        user_input = float(input("How much did the customer give you?"))

        if user_input >= customer_bill_total:
            amount_paid = user_input
        else:
            print("Customer must give you an amount more than or equal to ", customer_bill_total)
            customer_pay()
    except ValueError:
        print("Amount can contain only numbers and decimal point")
        customer_pay()

def amount_customer_paid():
    balance = (amount_paid - customer_bill_total)
    print(f"Amount Paid: {amount_paid: >10.2f} \nBalance: {balance: >10.2f}")

def receipt():
    restore()
    heading_info()
    double_design()
    header_printer()
    single_design()
    list_printing()
    single_design()
    sub_total_total()
    double_design()
    bill_total()
    amount_customer_paid()
    double_design()
    print("\t\t\tTHANK YOU FOR YOUR PATRONAGE")
    double_design()





if __name__ == '__main__':
    start_info_input()
    bill_page()
    receipt()

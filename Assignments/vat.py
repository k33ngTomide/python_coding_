

def your_vat(item_price: float, vat: float) -> float:
    value = item_price * (vat/100)
    return item_price + value

def exception_checker():
    try:
        user_price = float(input("Enter the price of item:  "))
        if user_price < 0: raise TypeError

        user_vat = float(input("Enter VAT:  "))
        if user_price > 0 and user_vat > 0:
            print(f"Total : {your_vat(user_price, user_vat)}")
        else:
            raise TypeError

    except ValueError:
        print("Invalid Input, Input only numbers, Try again")
        exception_checker()
    except TypeError:
        print("Price or VAT cannot be a Negative, Try Again")
        exception_checker()

if __name__ == '__main__':
    exception_checker()
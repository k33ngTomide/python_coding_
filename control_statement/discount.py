
price = int(input("Enter the price of the product:  "))
credit_score = int(input("Enter 1 for good credit score or 2 for bad credit score:  "))

if credit_score == 1:
    discount = (10/100) * price
    new_price = price - discount
    down_payment = new_price * (10/100)
    print("Your credit score is good, you got a 10% discount. "
          "\nYour discount is: ", discount,
          "\nYour down payment is: ", down_payment)
else:
    down_payment = price * (25/100)
    print("Your credit score is bad."
          "\nYour down payment", down_payment)
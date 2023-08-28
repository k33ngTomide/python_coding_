
coins = int(input('Enter your purchase price:  '))

if 0 < coins < 100:
    change = 100 - coins

    # for price in range():
    quarters = change//25
    # nickel = change % 25 // 20
    dime = change % 25 // 10
    penny = change % 25 % 10

    print(f'Your change is '
       f'\n {quarters} quarters'
       # f'\n {nickel} nickel'
       f'\n {dime} dime'
       f'\n{penny} penny')
else:
    print('invalid input')

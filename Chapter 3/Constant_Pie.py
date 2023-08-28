pie = 4
sign = -1

ap_pie_29 = 3.141592653589793238

# user_entry = int(input('Enter the number of term: '))
print('Term\t\tApprx. value of pie')


for value in range(3, 10000, 2):
    pie += (4 / value) * sign
    sign *= -1

    if pie == ap_pie:
        print(f'{value}\t\t{pie}')
        break

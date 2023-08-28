
# with open('../account.txt', mode='w') as my_file: //To write in the former directory



# with open('account.txt', mode='w') as my_file:
#     my_file.write('SN   NAME      SCORE  STATE    PLACE\n')
#     my_file.write('001: Tomide    57     Lagos    Sabo, Yabo\n')
#     my_file.write('002: Muiliyu   45     Abuja    Gwagwalada\n')
#     my_file.write('003: Mide      67     AkwaIbom Uyo\n')
#     my_file.write('004: Akin      23     Osun     Oshogbo\n')
#     my_file.write('005: Tommy     18     Imo      Owerri\n')
#     my_file.write('006: Tommie    45     Oyo      Ibadan\n')
#     my_file.write('007: Sodiq     23     Adamawa  Yola\n')



# with open('account.txt', mode='r') as my_file:
#     print(my_file.read())
#

file_obj = open('account.txt', mode='r')
print(file_obj.read())
file_obj.close()


# file_obj = open('account.txt', mode='r')
# print(file_obj.readlines())
# file_obj.seek(0)
# print(file_obj.readlines())
# file_obj.close()
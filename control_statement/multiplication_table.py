# def multiplication_table(end):
#     for a in range(1, 13):
#         for b in range(1, 13):
#             if a == 1:
#                 print("")
#                 c = 1
#                 while c <= size:
#                     print("\t\t %i x %i  = %-10i" % (a * c, b, ((a * c) * b)), end='')
#                     c += 1

def multiplication_table(end):
    for a in range(1, 13):
        print()
        for b in range(1, end + 1):
            print("%i x %i  = %-3i" % (b, a, (a * b)), end='\t\t')


multiplication_table(30)

# def multiplication_table(size):
#     a = 1
#     while a < 13:
#         print()
#         b = 1
#         while b <= size:
#             print("%i x %i  = %-3i" % (b, a, (a * b)), end='\t\t')
#             b = b + 1
#         a = a + 1
#


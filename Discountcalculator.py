receipt = float(input("Write the receipt price> "))
discount = float(input("write the discount % for the next visit> "))
finalprice=''

def discountprice( receipt, discount):
    finalprice = receipt * ((100-discount)/100)
    return finalprice

finalprice= discountprice( receipt, discount)
print(finalprice)


# #def x(y,z)
# a = formula
# return a

# a =x(y,z)
# print a
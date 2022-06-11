def discount(pr):
    pr = pr - (pr * 10) / 100
    return pr


def add_discount(newpr):
    newpr = newpr - (newpr * 10) / 100
    return newpr


price =int( input("enter the price :"))
y=float((add_discount(discount(price))))
print(y)

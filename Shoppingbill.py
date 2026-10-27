def calculateElectronicsGST(a, b):
    amount = a + b
    return amount + (amount * 18 / 100)


def calculateFashionGST(c, d):
    amount = c + d
    return amount + (amount * 13 / 100)


def calculateFoodGST(e):
    return e + (e * 7 / 100)


def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)

    return electronics + fashion + food


def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100
    return total - discount


# Sample test values
a = 100
b = 100
c = 100
d = 100
e = 100

electronics = calculateElectronicsGST(a, b)
fashion = calculateFashionGST(c, d)
food = calculateFoodGST(e)
total = totalBill(a, b, c, d, e)
discount = total * 20 / 100
final_amount = calculateDiscountedBill(a, b, c, d, e)

print("Electronics Bill:", f"{electronics:.2f}")
print("Fashion Bill:", f"{fashion:.2f}")
print("Food Bill:", f"{food:.2f}")
print("Total after GST:", f"{total:.2f}")
print("20% Discount:", f"{discount:.2f}")
print("Final Payable Amount:", f"{final_amount:.2f}")
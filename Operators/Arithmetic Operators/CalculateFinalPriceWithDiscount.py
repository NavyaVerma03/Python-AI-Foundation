#  Take price and discount %, calculate final price.

price = float(input("Enter price: "))
discount = float(input("Enter discount percentage: "))

final_price = price - (price * discount / 100)

print("Final Price =", final_price)
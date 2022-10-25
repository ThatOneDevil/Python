# 9/2/2022
# Order

total = 0
amount = int(input("Enter the amount of drinks you want to buy!"))
coinValue = int(input("Instert the money please"))
total = total + coinValue
price = 1.5*amount

while total < price:
    total = total + coinValue
    print("Please add more money") #asks for more money
    coinValue = float(input(""))
if total >= price:
    change = total - price # calculates the total
    print("Dispensed", amount, "drinks for", price)
    print("Change" + str(change)) # prints change


    

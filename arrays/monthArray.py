#Creating a numpy array 
#03/11/21

import numpy as np

sales = np.array([[0,0,0,0,0],
                 [0,0,0,0,0],
                 [0,0,0,0,0]])

totalSales = np.array([0,0,0,0,0])

for product in range(0,5):
    print("Sales for product " + str(product+1))
    for month in range(0,3):
        sales[month,product] = input("Enter Quantity for month " + str(month + 1) + ": ")
        totalSales[product] = totalSales[product]+sales[product,month-1]

print(totalSales)
print(sales)

    


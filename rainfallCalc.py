#13/10/21
#rainfall calc

month = ["January", "Febuary", "March", "april", "may", "june", "july", "august", "septembre", "october", "november", "december"]
rainFall = []
print("Please enter the value for following months: ")
for i in range(0,12):
    print(month[i])
    rainn = float(input(""))
    rainFall.append(rainn)
total = 0
for i in range(0,12):
    total += rainFall[i]
average = total/12
n_over_average = 0
for i in range(0,12):
    if rainFall[i] > average:
        n_over_average += 1
    else:
        pass
for i in range(0,12):
    print(month[i],rainFall[i])
print("The total rainfall for this year is: ", total)
print("The average rainfall for this year is: ", average)
print("The total rainfall for this year is: ", n_over_average)


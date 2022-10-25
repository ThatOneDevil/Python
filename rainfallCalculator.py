#13/10/2021
#rainfall calc
import numpy

array=numpy.array
month=array(["January","February","March","April","May","June","July","August","September","October","November","December"])
rain=array([])
print("please enter the value for the following months:")

for i in range(0,12):
    rainn=input(month[i])
    numpy.append(rain,rainn,axis=0)
    print(rain[1])
total=0

for i in range(1,11):
    total+=rain[i]

average=total/12
n_over_average=0

for i in range(0,12):
    if rain[i]>average:
        n_over_average+=1
    else:
        pass
for i in range(0,12):
    print(month[i],":     ",rain[i])

print("the total rainfall for this year is",total)
print("the average rainfall for this year is",average)
print("the number of months with above average rainfall is",n_over_average)

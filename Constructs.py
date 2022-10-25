#13/09/2021
#Times table using for and while loop

#For loop

ammount = int(input("Pleas enter the times table you want to display up to: "))
times = int(input("Please enter the times table u want: "))

for i in range (1,ammount + 1):
    answer = i*i
    print(i, "x", i, "=", answer)
    i = i + 1

#i = times   
#while i < ammount:
    #answer = i*i
    #print(i, "x", i, "=", answer)
    #i = i + 1

#22/10/21
#Procedure times table

def timestable(num):
    for i in range(0,13):
        answer=num*i
        print(num, "x", i, "=", answer)
        

num = int(input("Enter the number to print out timestable: "))
timestable(num)

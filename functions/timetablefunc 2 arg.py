#22/10/21
#Procedure times table with 2 args

def timestable(num, num2):
    for i in range(0,num2):
        answer=num*i
        print(num, "x", i, "=", answer)
        
def check(x):
    while x > 101 or x<0:
        x = int(input("Please type it in range of 12!"))
    return x


num = int(input("Enter the number to x by: "))
num2 = int(input("Enter the number to print out timestable up to: "))
num = check(num)
num2 = check(num2)
timestable(num, num2)

for i in range(10,0,-1):
    print(i)   


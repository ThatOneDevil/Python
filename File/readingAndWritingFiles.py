# 25/03/22
# Reading and writing files



file = open("information.txt", "a")
name = input("Enter your name: ")
DOB = input("Enter your date of birth: ")
file.write(name + ", " + DOB + "\n")
filer=open("information.txt", "r")
print(filer.read())
file.close()
filer.close()

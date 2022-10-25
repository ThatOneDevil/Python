import os
import csv

fileExists = os.path.exists('data.csv')
if fileExists == False:
    file = open("Python\data.csv", encoding='UTF8')
    file.close()  

name = ""

def makeFirstLetterCap(s):
    firstchar = s[:1]
    otherstring = s.replace(firstchar, "")
    return str.upper(firstchar) + str.lower(otherstring)

while len(name) != 2:
    name = input("Enter your name and surname: ")
    name = name.split(" ")
else:
    print(str.upper(name[0]), makeFirstLetterCap(str.upper(name[1])))
    with open('data.csv', 'a', encoding='UTF8') as file:
        nameArray = [str.upper(name[0]), makeFirstLetterCap(str.upper(name[1]))]
        csvWriter = csv.writer(file)
        csvWriter.writerow(nameArray)
        file.close()




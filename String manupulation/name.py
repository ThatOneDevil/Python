name = input("Enter your name: ")

name = name.split(" ")

forname = str.upper(name[0])
surname = str.upper(name[1])

def makeFirstLetterCap(s):
    firstchar = s[:1]
    otherstring = s.replace(firstchar, "")
    return str.upper(firstchar) + str.lower(otherstring)

print(makeFirstLetterCap(forname), makeFirstLetterCap(surname))

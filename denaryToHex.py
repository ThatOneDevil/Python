# 20/5/22
# Denary to hex


def numToLetter(denary):
    letters=["A","B","C","D","E","F"]
    if denary > 9:
        for i in range(0,6):
            if denary - i == 10:
                return letters[i]
    else:
        return denary

    return (denaryToHex(denary))
    
def denaryToHex(denary):
    while denary > 255 or denary < 0:
        denary = int(input("Enter a denary value: "))
    modD=denary % 16
    divD=denary // 16
    letter = str(numToLetter(divD))
    ones = str(numToLetter(modD))
    return (letter+ones)


def hexToDenary(hex):
    numbers=["10","11","12","13","14","15"]
    letters=["A","B","C","D","E","F"]
    if hex != range(1,9):
        for i in range(0,6):
            if letters[i] == hex:
                return numbers[i]
    else:
        return hex

denary = (int(input("Enter a denary value: ")))
hex = print(numToLetter(denary))
print(hexToDenary("A"))



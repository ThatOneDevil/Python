#25/05/2022

def hexNumber(l):
    numbers = ["10","11","12","13","14","15"]
    letters=["A","B","C","D","E","F"]
    if l != 1-9:
        for i in range(0,6):
            if letters[i] == l:
                return numbers[i]
    else:
        return l
hexd=("enter hex: ")
firstH=hexd[0]
secondH=hexd[1]

firstH=hexNumber(firstH)
firstH=int(firstH)
firstH=firstH*16
secondH=hexNumber(secondH)
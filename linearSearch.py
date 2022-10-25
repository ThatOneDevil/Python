# linear search with while and foor loop
# 11/3/22


whatToFind = int(input("Enter the number you want to find in the list: "))

list = [1,2,3,4,5]
found = False
index = 0

for i in range(0,len(list)):
    if whatToFind == list[i]:
        index = i
        found = True
    else:
        pass

if found == True:
    print("Found at",whatToFind, index)
else:
    print("not found")

while found == False and i<len(list):
    i = i+1
    if whatToFind == list[i]:
        index = i
        found = True
    else:
        pass

if found == True:
    print("Found at",whatToFind,index)
else:
    print("not found")

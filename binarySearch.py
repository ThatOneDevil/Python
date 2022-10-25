# Binary search
# 16/03/22

seq = ["A", "B", "C", "D", "E", "F", "G", "H"]
item = "A"
begin = 0
end = len(seq) - 1
found = False
q = 0

while begin <= end and found == False:
    mid = (begin + end) //2
    midValue = seq[mid]
    if midValue == item:
        print("The index position of the letter is", mid)
        found = True
    elif midValue > item:
        end = mid - 1
    elif midValue < item:
        begin = mid + 1
if found == False:
    for i in range(0, len(seq)):
        if seq[i] != item:
            q = q+1
        if q == len(seq):
            print("Item not found")

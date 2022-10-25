#08/10/21
#Creating a while loop with scores then printing highest int

while moreScores == True:
    score = int(input("Enter the next score, -1 to end: "))
    if score != -1: 
        numScore = numScore + 1
        totalScore = totalScore + score
        array.append(score) 
    else:
        moreScores = False
        print("No scores enterd - program ended")
        averageScore = totalScore/numScore
        print("AverageScore: ", averageScore)
        print("The largest number is: ", max(array))
        print("The smallest number is: ",min(array))

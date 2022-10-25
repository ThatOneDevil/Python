#08/10/21
#Creating a while loop with scores then printing

totalScore = 0
numScore = 0
moreScores = True
averageScore = 0
score = 0


while moreScores == True:
    score = int(input("Enter the next score, -1 to end: "))
    if score != -1: 
        numScore = numScore + 1
        totalScore = totalScore + score
    else:
        moreScores = False
        print("No scores enterd - program ended")
        averageScore = totalScore/numScore
        print("AverageScore: ", averageScore)


        

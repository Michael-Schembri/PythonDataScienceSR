import sklearn.neighbors as nb
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

def trainNearestNeighbor(dataSet, validationSet, nbrs = 5) :
    trainingSet = dataSet[["Height", "Weight", "ShoeSize"]]
    trainingLabels = dataSet["Label"]
    classifier = nb.KNeighborsClassifier(nbrs) 
    classifier = classifier.fit(trainingSet, trainingLabels)
    
    validationSet["Predicted"] = classifier.predict(validationSet[["Height", "Weight", "ShoeSize"]])
    validationSet["Match"] = validationSet["Label"] == validationSet["Predicted"]

    correctlyMatched = validationSet[validationSet["Match"]==True]
    percentage = len(correctlyMatched.index) / len(validationSet.index)
    return percentage

dataSet = pd.read_csv("Lesson1\\DataSets\\trainingSet.csv")
mds = dataSet[dataSet["Label"] == "male"]
fds = dataSet[dataSet["Label"] == "female"]

validationDataSet = pd.read_csv("Lesson1\\DataSets\\validationSet.csv")

max = 30
x = np.arange(5,max+1,1)
square = lambda x : x*x
x2 = square(x) 

resultsDF = pd.DataFrame(columns=["TrainingSetSize", "NumNeighbors","PercentageMatch"])

ns = [1, 3, 5, 9, 15]

for p in x2:
    q = math.ceil(p/2)
    subSet = pd.concat([mds.head(q), fds.head(q)], ignore_index=True)
    for n in ns:
        perc = trainNearestNeighbor(subSet, validationDataSet, n)
        resultsDF = resultsDF.append({"TrainingSetSize":p, "NumNeighbors":n,"PercentageMatch":perc}, ignore_index=True)

for n in ns:
    curX = resultsDF["TrainingSetSize"][resultsDF["NumNeighbors"]==n]
    curP = resultsDF["PercentageMatch"][resultsDF["NumNeighbors"]==n]
    plt.plot(curX, curP , linestyle='-', marker='x', label='{0} neighbors'.format(n))
    
plt.title("nearest neighbors, training set size to rate match")
plt.xlabel('Training set size')
plt.ylabel('Percentage match')
plt.legend()
plt.show()

# seems to stabilize at x= ~15, depending on number of neighbors. 
# the jump from 3>5 was approximately as large as 5>15. 
# there seems to be a point of diminishing returns
# this algorithm also performs well due to the evenness of the data and the fact that all factors play an equal role in classification
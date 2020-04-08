import sklearn.tree as tree
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

def trainDecisionTree(dataSet, validationSet) :
    trainingSet = dataSet[["Height", "Weight", "ShoeSize"]]
    trainingLabels = dataSet["Label"]
    classifier = tree.DecisionTreeClassifier() 
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

max = 38
x = np.arange(2,max+1,1)
square = lambda x : x*x
x2 = square(x) 

resultsDF = pd.DataFrame(columns=["TrainingSetSize","PercentageMatch"])

for p in x2:
    q = math.ceil(p/2)
    subSet = pd.concat([mds.head(q), fds.head(q)], ignore_index=True)
    perc = trainDecisionTree(subSet, validationDataSet)
    resultsDF = resultsDF.append({"TrainingSetSize":p,"PercentageMatch":perc}, ignore_index=True)
resultsDF.head()

#print (resultsDF)

plt.plot(x2, resultsDF["PercentageMatch"], linestyle='-', marker='x')
plt.title("Decision tree, training set size to rate match")
plt.xlabel('Training set size')
plt.ylabel('Percentage match')
#plt.xscale("log")
plt.show()

# seems to stabilize at x= ~35

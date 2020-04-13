import sklearn.neural_network as nn
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

def trainMLPNN(dataSet, validationSet) :
    trainingSet = dataSet[["Height", "Weight", "ShoeSize"]]
    trainingLabels = dataSet["Label"]
    classifier = nn.MLPClassifier(max_iter=600, solver='lbfgs',learning_rate='adaptive') 
    classifier = classifier.fit(trainingSet, trainingLabels)
    
    validationSet["Predicted"] = classifier.predict(validationSet[["Height", "Weight", "ShoeSize"]])
    validationSet["Match"] = validationSet["Label"] == validationSet["Predicted"]

    correctlyMatched = validationSet[validationSet["Match"]==True]
    percentage = len(correctlyMatched.index) / len(validationSet.index)
    return percentage

def trainMLPNNscore(dataSet, validationSet) :
    trainingSet = dataSet[["Height", "Weight", "ShoeSize"]]
    trainingLabels = dataSet["Label"]
    #classifier = nn.MLPClassifier(max_iter=300, solver='sgd', learning_rate='adaptive', hidden_layer_sizes=[100, 100]) 
    classifier = nn.MLPClassifier(max_iter=12000, solver='lbfgs',learning_rate='adaptive',early_stopping=True) 
    #classifier = nn.MLPClassifier(max_iter=900, solver='lbfgs',hidden_layer_sizes=[100, 100]) 
    classifier = classifier.fit(trainingSet, trainingLabels)
    
    return classifier.score(validationSet[["Height", "Weight", "ShoeSize"]], validationSet["Label"])

dataSet = pd.read_csv("Lesson1\\DataSets\\trainingSet.csv")
mds = dataSet[dataSet["Label"] == "male"]
fds = dataSet[dataSet["Label"] == "female"]

validationDataSet = pd.read_csv("Lesson1\\DataSets\\validationSet.csv")

max =60
x = np.arange(30,max+1,5)
square = lambda x : x*x
x2 = square(x) 

resultsDF = pd.DataFrame(columns=["TrainingSetSize","PercentageMatch"])

for p in x2:
    q = math.ceil(p/2)
    subSet = pd.concat([mds.head(q), fds.head(q)], ignore_index=True)
    perc = trainMLPNNscore(subSet, validationDataSet)
    resultsDF = resultsDF.append({"TrainingSetSize":p,"PercentageMatch":perc}, ignore_index=True)
resultsDF.head()

#print (resultsDF)

plt.plot(x2, resultsDF["PercentageMatch"], linestyle='-', marker='x')
plt.title("Decision tree, training set size to rate match")
plt.xlabel('Training set size')
plt.ylabel('Percentage match')
#plt.xscale("log")
plt.show()
 

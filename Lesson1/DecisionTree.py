import sklearn.tree as tree
import pandas as pd

dataSet = pd.read_csv("Lesson1\\DataSets\\trainingSet.csv")

trainingSet = dataSet[["Height", "Weight", "ShoeSize"]]
trainingLabels = dataSet["Label"]

classifier = tree.DecisionTreeClassifier() 
classifier = classifier.fit(trainingSet, trainingLabels)

validationDF = pd.read_csv("Lesson1\\DataSets\\validationSet.csv")
validationDF["Predicted"] = classifier.predict(validationDF[["Height", "Weight", "ShoeSize"]])
validationDF["Match"] = validationDF["Label"] == validationDF["Predicted"]

correctlyMatched = validationDF[validationDF["Match"]==True]
percentage = len(correctlyMatched.index) / len(validationDF.index)
print("{0}%".format(percentage*100))
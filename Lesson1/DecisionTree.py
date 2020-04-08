import sklearn.tree as tree
import generateDataSet as ds

dataSet = ds.generate(100000)

trainingSet = dataSet[["Height", "Weight", "ShoeSize"]]
trainingLabels = dataSet["Label"]

classifier = tree.DecisionTreeClassifier() 
classifier = classifier.fit(trainingSet, trainingLabels)

validationDF = ds.generate(100000,55)
validationDF["Predicted"] = classifier.predict(validationDF[["Height", "Weight", "ShoeSize"]])
validationDF["Match"] = validationDF["Label"] == validationDF["Predicted"]

#print(dataSet)
#print(validationDF)
correctlyMatched = validationDF[validationDF["Match"]==True]
percentage = len(correctlyMatched.index) / len(validationDF.index)
print("{0}%".format(percentage*100))
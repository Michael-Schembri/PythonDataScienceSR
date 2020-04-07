import sklearn.tree as tree
import generateDataSet as ds

dataSet = ds.generate(1000)

trainingSet = dataSet[["Height", "Weight", "ShoeSize"]]
trainingLabels = dataSet["Label"]

classifier = tree.DecisionTreeClassifier() 
classifier = classifier.fit(trainingSet, trainingLabels)

# should always return male and female.
validationSet = [[182, 70, 45], [155, 49, 34]]

prediction = classifier.predict(validationSet)
print(prediction)
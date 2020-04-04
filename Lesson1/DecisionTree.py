from sklearn import tree

classifier = tree.DecisionTreeClassifier()

#list of lists, with each list containing [Height (cm), Weight (kg) and Shoe Size (european)]
trainingSet = [[181, 80, 44], [177, 70, 43], [160, 60, 38],[154, 54, 37], [166, 65, 40],[190, 90, 47], [175, 64, 39],[177, 70, 40], 
            [159, 55, 37], [171, 75, 42], [181, 85, 43]]

TraininSetLabels = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female','female', 'male', 'male']
 
classifier = classifier.fit(trainingSet, TraininSetLabels)

prediction = classifier.predict([[182, 70, 45]])


print(prediction)
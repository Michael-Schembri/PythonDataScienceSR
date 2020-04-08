import pandas as pd
import generateDataSet as ds

trainingSet = ds.generate(10000, 0)
trainingSet.to_csv('Lesson1\\DataSets\\trainingSet.csv', index=False)

validationSet = ds.generate(10000, 0)
validationSet.to_csv('Lesson1\\DataSets\\validationSet.csv', index=False)
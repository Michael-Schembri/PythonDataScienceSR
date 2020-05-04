import generateDataSet as ds
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#dataSet = pd.read_csv("Lesson1\\DataSets\\validationSet.csv")
dataSet = pd.read_csv("Lesson1\\DataSets\\trainingSet.csv")
#marker = lambda label : 'x' if (label == 'female') else 'o'
#dataSet["Marker"] = marker([dataSet["Label"]])
 
mds = dataSet[dataSet["Label"] == "male"]
fds = dataSet[dataSet["Label"] == "female"]

threedee = plt.figure().gca(projection='3d')
threedee.scatter(mds['Height'], mds['Weight'], mds['ShoeSize'], marker ='x')
threedee.scatter(fds['Height'], fds['Weight'], fds['ShoeSize'], marker = 'o')
threedee.set_xlabel('Height')
threedee.set_ylabel('Weight')
threedee.set_zlabel('ShoeSize')

plt.show()

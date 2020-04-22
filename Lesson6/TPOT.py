import pandas as pd
from tpot import TPOTClassifier
import numpy as np


dataSet = pd.read_csv("Lesson1\\DataSets\\trainingSet.csv")
dataSet_shuffle = dataSet.iloc[(np.random.permutation(len(dataSet)))]
ds = dataSet_shuffle.reset_index(drop = True)
ds['MappedLabel'] = ds['Label'].map({'male':1,'female':0})
#print(ds.head())
pipeline_optimizer = TPOTClassifier(generations=5, population_size=30, cv=5, random_state=42, verbosity=2)
pipeline_optimizer.fit(ds[['Height','Weight','ShoeSize']], ds['MappedLabel'])

print(pipeline_optimizer.score(ds[['Height','Weight','ShoeSize']], ds['MappedLabel']))

pipeline_optimizer.export('Lesson6\\pipeline.py')
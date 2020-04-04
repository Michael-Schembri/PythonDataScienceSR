# This import registers the 3D projection, but is otherwise unused.
import mpl_toolkits.mplot3d as Axes3D
import matplotlib.pyplot as plt
import numpy as np
 
 
trainingSet = [[181, 80, 44], [177, 70, 43], [160, 60, 38],[154, 54, 37], [166, 65, 40],[190, 90, 47], [175, 64, 39],[177, 70, 40], 
            [159, 55, 37], [171, 75, 42], [181, 85, 43]]

TrainingSetLabels = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female','female', 'male', 'male']
 
#there's probably a better way to do this than to fuse the sets manually  
trainingSetMarkers = [[181, 80, 44,'o'], [177, 70, 43,'o'], [160, 60, 38,'x'],[154, 54, 37,'x'], [166, 65, 40,'o'],[190, 90, 47,'o'], [175, 64, 39, 'x'],[177, 70, 40, 'x'], 
            [159, 55, 37, 'x'], [171, 75, 42,'o'], [181, 85, 43,'o']]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') 

#loop over all elements in trainingset markers
for x, y, z, m in trainingSetMarkers:
    ax.scatter(x, y, z, marker=m)

ax.set_xlabel('height')
ax.set_ylabel('weight')
ax.set_zlabel('shoe size')

plt.show()
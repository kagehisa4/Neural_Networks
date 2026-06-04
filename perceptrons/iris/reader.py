#This is scatter plot for feature number 1 & 3 from
# The IRIS dataset.  Courtesy- UCL
#Training data : first 100 rows
# Test data: last 50 rows

#first_row = df.iloc[0:5, [0,2]]
 #This returns a list y = df.iloc[:100, 4].values

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('iris.data')
#Create target variable Y
#Obtain list of feature values

#assign Iris-setosa : 1 else -1
#Obtain input data and target data
y = []
x = []
for i in range(100):
    lst = []
    if df.iloc[i,4] != 'Iris-setosa': # EDIT TO CHANGE FEATURE CLASS
        y.append(-1)
    else:
        y.append(1)
    x.append(df.iloc[i, [0,2]]) # EDIT [0,2] TO CHANGE INPUT FEATURE

X = np.array(x)
X = X.reshape(100,2)
# code to obtain plots:
'''
plt.scatter(X[:50, 0], X[:50, 1], color = 'red', marker = 'o', label = 'setosa')
plt.scatter(X[50:, 0], X[50:, 1], color = 'blue', marker = 'x', label = 'versicolor')

#make plots
plt.xlabel('sepal length')
plt.ylabel('petal length')
plt.legend(loc = 'upper left')
plt.show()
'''

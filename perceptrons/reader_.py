#This is scatter plot for feature number 1 & 3 from
# The IRIS dataset.  Courtesy- UCL
#Training data : first 100 rows
# Test data: last 50 rows

#first_row = df.iloc[0:5, [0,2]]
 #This returns a list y = df.iloc[:100, 4].values


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('iris.data')

#Create target variable Y
#Obtain list of feature values

#assign Iris-setosa : 1 else -1

lst = []
for i in range(100):
    if df.iloc[i,4] != 'Iris-setosa':
        lst.append(-1)
    else:
        lst.append(1)
    #plot scatters-
    if i ==0:
        plt.scatter(df.iloc[i,0], df.iloc[i,2], color='red', label='setosa', marker='o')
    elif i<50:
        plt.scatter(df.iloc[i,0], df.iloc[i,2], color='red', marker='o')
    elif i ==50:
        plt.scatter(df.iloc[i,0], df.iloc[i,2], color='blue', label='versicolor', marker='x')
    else:
        plt.scatter(df.iloc[i,0], df.iloc[i,2], color='blue', marker='x')

#make plots
plt.xlabel('sepal length')
plt.ylabel('petal length')
plt.legend(loc = 'upper left')
plt.show()

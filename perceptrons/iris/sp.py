import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('iris.csv')

for i in range(50,100):
    if i ==50:
        plt.scatter(df['sl'].iloc[i], df['pw'].iloc[i],
        marker = 'o', color = 'green', alpha = .8,
        label = 'iris-versicolor')
    plt.scatter(df['sl'].iloc[i], df['pw'].iloc[i],
        marker = 'o', color = 'green', alpha = .8,
        )
for i in range(100, 150):
    if i ==100:
        plt.scatter(df['sl'].iloc[i], df['pw'].iloc[i],
        marker = 'x', color = 'red', alpha = .8,
        label = 'iris-verginica')
    else:
        plt.scatter(df['sl'].iloc[i], df['pw'].iloc[i],
        marker = 'x', color = 'red', alpha = .8,
        )

plt.xlabel('sepal length')
plt.ylabel('petal width')
plt.legend(loc = 'best')
plt.show()

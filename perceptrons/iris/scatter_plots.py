import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('iris.csv')

for i in range(50):
    if i ==0:
        plt.scatter(df['sw'].iloc[i], df['pl'].iloc[i],
        marker = 'o', color = 'green', alpha = .8,
        label = 'iris-setosa')
    plt.scatter(df['sw'].iloc[i], df['pl'].iloc[i],
        marker = 'o', color = 'green', alpha = .8,
        )
for i in range(50,100):
    if i == 50:
        plt.scatter(df['sw'].iloc[i], df['pl'].iloc[i],
        marker = 'x', color = 'red', alpha = .8,
        label = 'iris-versicolor')
    else:
        plt.scatter(df['sw'].iloc[i], df['pl'].iloc[i],
        marker = 'x', color = 'red', alpha = .8,
        )

plt.xlabel('petal length')
plt.ylabel('petal width')
plt.legend(loc = 'best')
plt.show()

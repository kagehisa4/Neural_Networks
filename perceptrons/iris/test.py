import pickle
import matplotlib.pyplot as plt
from drs import plot_decision_regions
import reader

with open("ppn.pkl", "rb") as f:
    ppn = pickle.load(f)

# test from user input
sl = float(input('sepal_length'))
pl = float(input('petal_length'))


output = ppn.predict([sl,pl])

print('Iris-serosa') if output == 1 else print('Iris-versicolor')

#print errors from the list:
plot_decision_regions(reader.X, reader.y, classifier = ppn)
plt.xlabel('sepal length (cm)')
plt.ylabel('petal length (cm)')
plt.legend(loc = 'upper left')
plt.show()

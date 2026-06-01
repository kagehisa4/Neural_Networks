import pickle
import matplotlib.pyplot as plt
from decision_region import plot_decision_regions
import reader

with open("ppn.pkl", "rb") as f:
    ppn = pickle.load(f)

# test
'''sl = float(input('sepal_l'))
pl = float(input('petal_l'))


output = ppn.predict([sl,pl])

print('Iris-serosa') if output == 1 else print('Iris-versicolor')'''

#print errors from the list:
plot_decision_regions(reader.X, reader.y, classifier = ppn)
plt.xlabel('sepal length (cm)')
plt.ylabel('petal length (cm)')
plt.legend(loc = 'upper left')
plt.show()

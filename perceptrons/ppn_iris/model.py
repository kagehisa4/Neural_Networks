import pickle
import matplotlib.pyplot as plt
# load model

with open("ppn.pkl", "rb") as f:
    ppn = pickle.load(f)

# test
'''sl = float(input('sepal_l'))
pl = float(input('petal_l'))


output = ppn.predict([sl,pl])

print('Iris-serosa') if output == 1 else print('Iris-versicolor')'''

#print errors from the list:
print(ppn.lg_rate)
plt.plot(range(1, len(ppn.errors_) + 1) , ppn.errors_ , marker = 'o', color = 'blue')
plt.xlabel('epoch number')
plt.ylabel('Misclassifications')
plt.show()

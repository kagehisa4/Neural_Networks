from matplotlib.colors import ListedColormap
import numpy as np
import  matplotlib.pyplot as plt

# plot decision region with this function

def plot_decision_regions(X,y,classifier,resolution=.02):
    # find minimum and maximum values in the dataset:
    x_max, x_min = np.array(X[:, 0]).max(), np.array(X[:, 0]).min()
    y_max, y_min = np.array(X[:, 1]).max(), np.array(X[:, 1]).min()

    # create grid

    x,y = np.meshgrid(np.arange(x_min, x_max, resolution), np.arange(y_min, y_max, resolution))

    # create values at the grid:

    z = classifier.predict(np.array([x.ravel(), y.ravel()]).T)
    z = z.reshape(x.shape)
    # create colormamp

    cmap = ListedColormap(('blue', 'green'))

    plt.contourf(x,y,z,cmap=cmap)

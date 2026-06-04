from matplotlib.colors import ListedColormap
import numpy as np
import  matplotlib.pyplot as plt

# plot decision region with this function

def plot_decision_regions(X,y,classifier,resolution=.02):
    # find minimum and maximum values in the dataset:
    x_max, x_min = np.array(X[:, 0]).max(), np.array(X[:, 0]).min()
    y_max, y_min = np.array(X[:, 1]).max(), np.array(X[:, 1]).min()

    # create grid

    xsl,ysl = np.meshgrid(np.arange(x_min -1, x_max +1, resolution), np.arange(y_min - 1, y_max +1, resolution))

    # create values at the grid:

    z = classifier.predict(np.array([xsl.ravel(), ysl.ravel()]).T)
    z = z.reshape(xsl.shape)
    # create colormamp

    cmap = ListedColormap(('red', 'green'))

    plt.contourf(xsl,ysl,z,cmap=cmap, alpha = .4)

    # plot scatter

    marker = ['x', 'o']
    for idx, vl in enumerate(np.unique(y)):

        plt.scatter(

        X[y==vl,0], X[y==vl,1], # array masking
        c = cmap(idx), alpha = .8, marker = marker[idx],
        label = vl

        )

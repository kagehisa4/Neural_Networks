from matplotlib.colors import ListedColormap
import numpy as np
import  matplotlib.pyplot as plt

def plot_decision_regions(X,y,classifier,resolution=.02):

    markers = ('s', 'x', 'o', '^', 'v')

    cmap = ListedColormap(('green', 'blue')) #maps values to colors

    #find out boundary values for both features
    sl_min, sl_max = X[:, 0].min(), X[:, 0].max()
    pl_min, pl_max = X[:, 1].min(), X[:, 1].max()

    # make grid objects for evenly spaced values:

    xsl, xpl = np.meshgrid(np.arange(sl_min, sl_max, resolution), np.arange(pl_min, pl_max, resolution))

    # create classifier boundary line

    b_l = classifier.predict(np.array([xsl.ravel(), xpl.ravel()]).T) #pass all grid points together.
    b_l= b_l.reshape(xsl.shape) # this give an array same shape as xsl, xpl


    plt.contourf(xsl, xpl, b_l, alpha=.2, cmap=cmap) # creats grid- map values & colors alpha- b/w 0 and 1.

    #define plot limits - offset by original min/max margins.
    plt.xlim(xsl.min() -.2, xsl.max() + .2)
    plt.ylim(xpl.min() -.2, xpl.max() + .2)

    # plot class samples
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter (x = X[y == cl, 0], y = X[ y == cl, 1], # only select rows where label are same.
            alpha = .8, c = cmap (idx),
            marker = markers[idx], label = cl)

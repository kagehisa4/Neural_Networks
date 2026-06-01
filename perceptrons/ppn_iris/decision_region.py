from matplotlib.colors import ListedColormap

def plot_decision_regions(X,y,classifier,resolution=.02):

    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')

    #find out boundary values for both features

    sl_min, sl_max = X[:, 0].min(), X[:, 0].max()
    pl_min, pl_max = X[:, 1].min(), X[:, 1].max()

    # make grid objects

    xsl = np.meshgrid(np.arange(sl_min, sl_max, resolution))
    xpl = np.meshgrid(np.arange(pl_min, pl_max, resolution))

    # create classifier boundary line

    b_l = classifier.predict(np.array([xsl.ravel(), xpl.ravel()]).T)
    b_l.reshape(xsl.shape)

    #define limits

    plt.contourf(xsl, xpl, b_l, alpha=.4, cmap=cmap)

    plt.xlim(xsl.min(), xsl.max())
    plt.ylim(xpl.min(), xpl.max())

    # plot class samples

    

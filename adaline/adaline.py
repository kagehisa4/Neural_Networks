# this code trains an ADALINE network on IRIS dataset

# define training parameters

class adaline (object):
    def __init__(self, n_iter, eta):
        self.n_iter = n_iter
        self.eta = eta


# define errors and weights
    self.w_ = np.zeros(1 + X.shape[1])
    self.e_ = np.zeros(len(X))

# define dot product function
    def dot_product(self,X):
        return np.dot(X, self.w_[1:])

# train the network based on batch GD
    def train(self,X,y):
        for i in range (self.n_iter):
            error = y - dot_product(X)
            self.w_[1:] += self.eta * X.T.dot(error)
            self.w_[0] += self.eta * error.sum()

    def predict(X,self):
        return np.where((dot_product(X) + self.w_[0]) >= 0.0, 1, -1 )

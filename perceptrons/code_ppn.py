# This is the code to train a Perceptron
import numpy as np

class Perceptron(object):
    def __init__(self,lg_rate,n_iter):
        self.lg_rate = lg_rate
        self.n_iter = n_iter

    #create fit function
    def fit(self,X,y):
        self.w_ = np.zeroes(1 + np.shape(X[1]))
        self.errors_ = []
        for _ in len(self.n_iter):
            errors_ = 0
            for row in range(len(X)):
                target = y(row)
                update = self.lg_rate * (target-self.predict(X))
                error_ += update
                self.w_[0] += update * 1
                self.w_[1:] += update * X[row, [0,2]]
            self.errors_.append(errors_)
        return self

    def product(self,X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self,X):
        return np.where(self.product(X) >= 0, 1, -1)

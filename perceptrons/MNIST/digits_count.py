from sklearn.datasets import load_digits
import sklearn

digits = load_digits()

X = digits.data
y = digits.target

hm = {}

digits = {0,1,2,3,4,5,6,7,8,9}

for i in range (len(y)):
    if y[i] not in hm:
        hm[int(y[i])] = 0
    if y[i] in digits:
        hm[y[i]] += 1

print(hm)

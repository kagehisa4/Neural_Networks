from sklearn.datasets import load_digits

digits = load_digits()

X = digits.data
y = digits.target

hm = {}

for i in range (len(y)):
    if y[i] not in hm:
        hm[int(y[i])] = 0
    hm[y[i]] += 1

print(hm)

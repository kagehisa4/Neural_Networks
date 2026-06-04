from ppn import Perceptron
import reader
import pickle

ppn = Perceptron(lg_rate = .01, n_iter = 10)


ppn.fit(reader.X,reader.y)

#Save
with open("ppn.pkl", "wb") as f:
    pickle.dump(ppn,f)

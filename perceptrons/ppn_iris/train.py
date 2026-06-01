from ppn import Perceptron
import reader
import pickle

ppn_ = Perceptron(1, 15)


ppn_.fit(reader.X,reader.y)

#Save
with open("ppn.pkl", "wb") as f:
    pickle.dump(ppn_,f)

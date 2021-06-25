from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from fractions import Fraction
import numpy as np
import pandas as pd
import mglearn
from sklearn.neighbors import KNeighborsClassifier

# np.set_printoptions(formatter={'all': lambda x: str(Fraction(x).limit_denominator())})

import sys
import numpy as np
import csv
class Data:
    def getData(self, filename):
        with open (filename) as file:
            f = csv.reader(file)
            next(f)
            data = []
            for row in f:
               data.append(row)
            return data

m = Data()
all_data = m.getData('iris.csv')
all_data_numpy = np.array(all_data)


train_x, test_x, train_y, test_y = train_test_split(all_data_numpy[:, :-1], all_data_numpy[:, -1:], test_size=5, random_state=0)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(train_x, train_y)

y_pred = knn.predict(test_x)
test_y = test_y.reshape(-1)
#print("test predictions: {}".format(y_pred))
np.ravel(test_y)

print("the rate:{}".format(np.mean(y_pred==test_y)))
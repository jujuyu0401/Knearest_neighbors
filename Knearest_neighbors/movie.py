import numpy as np
import operator


def createDataSet():
    ary = np.array([[3, 104],
           [2, 100],
           [1., 81],
           [101., 10],
           [99, 5],
           [98, 2]])
    labels = ['love', 'love', 'love', 'action', 'action', 'action']
    return ary, labels

def calculate(train_feature, train_labels, test):
    for i in range(train_feature.shape[0]):
        train_feature[i] -= test

    print(train_feature)
    dif = train_feature ** 2
    dif = np.sum(dif, axis=1)

    labels_list = []
    for i in range(dif.shape[0]):
        labels_list.append((dif[i], train_labels[i]))
    labels_list.sort(key=lambda x: x[0])


    labels_dictionary = {}
    for i in range(5):
        labels_dictionary[labels_list[i][1]] = 0

    for i in range(3):
        labels_dictionary[labels_list[i][1]] += 1

    ret = max(labels_dictionary, key=lambda x:labels_dictionary[x])
    return ret


ary, labels = createDataSet()
labels_cpy = [1, 1, 1, 2, 2, 2]
''' sklearn classifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

ary, labels = createDataSet()
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(ary, labels)
print(knn.predict([[18, 90]]))
'''


import matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()
plt.xlabel("action")
plt.ylabel("kisses")
ax = fig.add_subplot(111)
ax.scatter(ary[:, 0], ary[:, 1], 15.0 * np.array(labels_cpy), 15.0 * np.array(labels_cpy))
# plt.show()



test = np.array([18, 90])
print(calculate(ary, labels, test))
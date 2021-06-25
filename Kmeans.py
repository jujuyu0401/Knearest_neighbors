import sys
sys.path.append('./pre_compile')

import csv
class Data:

    def getData(self, filename):
        with open (filename) as file:
           f = csv.reader(file)

           next(f)
           for row in f:
             print(row)


# m = Data()
# m.getData('iris.csv')

import pre_works.pre_works
# import random
# i = 0
# girls = 0
# boys = 0
# while i < 10000:
#     a = random.randint(1, 2)
#     if a == 1:
#         girls = girls + 1
#     elif a == 2:
#         boys = boys + 1
#         i = i + 1
#
# print('girls: ' + str(girls))
# print('boys:'+ str(boys))
# print(girls / (girls + boys))

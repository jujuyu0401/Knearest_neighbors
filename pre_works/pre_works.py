import numpy as np
from scipy import stats
ary = np.array([[1, 2, 5],
              [9, 9, 3],
              [5, 34, 66],
              [1, 33, 21]])

a = [(1, 2),
     (9, 9),
     (5, 34),
     (1, 33)]

print(a.sort(key=lambda x:x[1]))

print(a)
# element = {}
# for i in range(100):
#     element[i] = 0
# for i in range(ary.shape[0]):
#     for j in range(ary.shape[1]):
#         element[ary[i][j]] += 1
#
# max_element = 0
# for key, value in element.items():
#     if value == max(element.values()):
#         max_element = key
#         break
#
# for i in range(ary.shape[0]):
#     for j in range(ary.shape[1]):
#         if (ary[i][j] < max_element + 10) & (ary[i][j] > max_element - 10):
#             ary[i][j] = 255
#         else:
#             ary[i][j] = 0
# print(ary)

#
# for i in range(ary_shape[0]):
#     for j in range(ary_shape[1]):
#         print("1")


# for i in np.nditer(c, op_flags = ['readwrite']):
#     if i < d + 10 & i > d - 10:
#         i *= 0
#     else:
#         i = 255.0
#
# print(c)
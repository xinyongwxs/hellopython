import kNN
from numpy import *
import matplotlib.pyplot as plt

# import matplotlib

# group, labels = kNN.createDataSet()

# print(kNN.classify0([0, 0], group, labels, 3))

# test = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# test0 = zeros((4, 3))
# test1 = array([array([1, 2, 3]), array([4, 5, 6]), array([7, 8, 9])])
# print(test0[2, :])
# print(test[2][:])
# print(test1[2, :])

# datingDataMat, datingLabels = kNN.file2matrix("datingTestSet2.txt")
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(
#     datingDataMat[:, 0],
#     datingDataMat[:, 1],
#     array(datingLabels),
#     10.0 * array(datingLabels),
# )
# plt.show()
# print(datingDataMat)
# print(datingLabels)

kNN.datingClassTest()

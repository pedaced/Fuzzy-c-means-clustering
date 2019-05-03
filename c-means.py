import numpy as np
import math

def dist(p1, p2):
	return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

#fcmeans function for Fuzzy clustering
def fcmeans(cluster_no, iteration_no, data):
	clusters = []
	n = len(data)
	mu = np.zeros((n, cluster_no))

	#Choosing random clusters
	for i in range(cluster_no):
		clusters.append([np.random.rand() * 10, np.random.rand() * 10])

	#algorithm iteration
	
	for it in range(iteration_no):
		for i in range(n):
			for j in range(cluster_no):
				temp = 0
				for k in range(cluster_no):  
					temp += dist(data[i], clusters[j]) ** 2 / dist(data[i], clusters[k]) ** 2
				mu[i][j] = 1 / temp

		for j in range(cluster_no):
			temp1 = temp2 = temp3 = 0
			for i in range(n):
				temp3 += mu[i][j] ** 2
				temp1 += (mu[i][j] ** 2) * data[i][0]
				temp2 += (mu[i][j] ** 2) * data[i][1]
			clusters[j][0] = temp1 / temp3
			clusters[j][1] = temp2 / temp3

	print(clusters)

#test functions via random data set and cluster numer.

c = 2
data_set = [[1, 3], [1.5, 3.2], [1.3, 2.6], [3, 1]]
iteration = 10
fcmeans(c, iteration, data_set)
# cluster_no = 3
# n = 200
# iteration_no = 100
# data_set = []
# for i in range(n):
# 	data_set.append([np.random.rand() * 10, np.random.rand() * 10])
# data_set[0][0] = 0
# print(data_set)
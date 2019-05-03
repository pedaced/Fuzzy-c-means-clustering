import numpy as np
import math
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt


def dist(p1, p2):
	return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

#fcmeans function for Fuzzy clustering
def fcmeans(cluster_no, iteration_no, data):
	clusters = []
	n = len(data)
	mu = np.zeros((n, cluster_no))
	colors = ['b', 'r', 'g', 'c', 'm', 'y', 'k']

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

	#drawing plot
	data_set1 = []
	data_set2 = []
	for i in range(n):
		data_set1.append(data[i][0])
		data_set2.append(data[i][1])

	fig = plt.figure()
	ax = fig.subplots()

	for j in range(n):	
		cluster = np.argmax(mu[j])
		membership = mu[j][cluster]
		plt.scatter(data_set1[j], data_set2[j], color = colors[cluster], alpha = membership)
	plt.show()
	plt.savefig("plot.png")	



#test functions via random data set and cluster numer.
cluster_no = 5
n = 2000
iteration_no = 100
data_set = []
for i in range(n):
	data_set.append([np.random.rand() * 10, np.random.rand() * 10])
fcmeans(cluster_no, iteration_no, data_set)

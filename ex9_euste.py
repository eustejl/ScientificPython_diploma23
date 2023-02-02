'''
    Implement k-means algorithm
    https://en.wikipedia.org/wiki/K-means_clustering
    
    load the s3.txt file\n",
    choose 15 random points wihin your data\n",
    compute the distance from those points to each point of the data\n",
    assign the points to the closest centroids\n",
    update the centroids as the center (mean) of all the coordinates\n",
    repeat the last 3 steps 100 times\n",
    plot the clusters and the final centroids"

'''

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

data = np.genfromtxt('s3.txt')
data = data/10000. # to make vaues more manageable

x,y = data.copy()[:,0],data.copy()[:,1]

# scatter plot to visualize
# plt.plot(x,y,'.')
# plt.show()

nr = 15 # number of centroids
N = len(x) # number of points
idx = np.random.choice(range(N),size=nr,replace=False) # index of random points

# plt.plot(x[idx],y[idx],'.')
# plt.show()

distances = np.empty(shape=(nr,N),dtype=float)
clusters = np.empty(N,dtype=int)
centroids = data.copy()[idx]



x_c,y_c = centroids.copy()[:,0],centroids.copy()[:,1]



max_iter = 100
for j in range(max_iter):
    # compute the distance from those points to each point of the data
    for i in range(nr):
        distances[i] = np.sqrt((x_c[i] - x)**2 + (y_c[i] - y)**2)
        
        
    # assign the points to the closest centroids
    clusters = np.argmin(distances,axis=0)
    
    
    # update the centroids as the center (mean) of all the coordinates
    for c in np.unique(clusters):
        centroids[c] = np.mean(data[clusters==c],axis=0)
    
    x_c,y_c = centroids.copy()[:,0],centroids.copy()[:,1]
    



for c in np.unique(clusters):
    plt.plot(x[clusters==c],y[clusters==c],'.')
plt.xlim(10,90)
plt.ylim(10,90)
plt.show()
        

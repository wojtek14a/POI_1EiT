from sklearn.cluster import KMeans, DBSCAN

import csv
import matplotlib.pyplot as plt
import numpy as np
import pyransac3d

def import_data(file):
    with open(file, newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for x, y, z in reader:
            yield (float(x), float(y), float(z))

if __name__ == "__main__":
    points = list(import_data("points.xyz"))

    # KMeans clustering

    clusterer = KMeans(n_clusters=3)

    X = np.array(points)
    ax = clusterer.fit_predict(X)

    cyan = ax == 0
    magenta = ax == 1
    yellow = ax == 2

    plot = plt.figure()
    axis = plot.add_subplot(projection="3d")
    axis.scatter(X[cyan, 0], X[cyan, 1], X[cyan, 2], c="cyan")
    axis.scatter(X[magenta, 0], X[magenta, 1], X[magenta, 2], c="magenta")
    axis.scatter(X[yellow, 0], X[yellow, 1], X[yellow, 2], c="yellow")
    plt.show()

    # DBSCAN clustering

    clustering = DBSCAN(eps=50, min_samples=10).fit_predict(X)
    cyan = clustering == 0
    magenta = clustering == 1
    yellow = clustering == 2

    plot2 = plt.figure()
    axis2 = plot2.add_subplot(projection="3d")
    axis2.scatter(X[cyan, 0], X[cyan, 1], X[cyan, 2], c="cyan")
    axis2.scatter(X[magenta, 0], X[magenta, 1], X[magenta, 2], c="magenta")
    axis2.scatter(X[yellow, 0], X[yellow, 1], X[yellow, 2], c="yellow")
    plt.show()
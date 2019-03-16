import numpy as np
import random
import scipy.stats as ss
import matplotlib.pyplot as plt
#from sklearn import datasets

p1 = np.array([1,1])
p2 = np.array([4,4])

def distance(p1, p2):
    dist = np.sqrt(np.sum(np.power(p2-p1, 2)))
    return dist

def majority_vote(votes):
    vote_counts = {}
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] = 1

    winners = []
    max_count = max(vote_counts.values())
    for vote, counts in vote_counts.items():
        if counts == max_count:
            winners.append(vote)

    return random.choice(winners)

def majority_vote_short(votes):
    mode, count = ss.mstats.mode(votes)
    return mode

votes = [1,2,3,1,2,3,1,2,3,3,3,3,2,2,2]

## Get the k-Nearest Neighbours of the point 'P'

# p = np.array([1,1.5])
# points = np.array([[1,1], [1,2], [1,3], [2,1], [2,2], [2,3], [3,1], [3,2], [3,3]])
# outcomes = np.array([0,0,0,0,1,1,1,1,1])

def findDistances (point, neighbouringPoints):
    distances = np.zeros(neighbouringPoints.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(point, neighbouringPoints[i])
    return distances

def findNearestNeighbours (point, neighbouringPoints, k):
    distances = findDistances(point, neighbouringPoints)
    sortedInd = np.argsort(distances)
    return sortedInd[:k]

def kNN (point, neighbouringPoints, outcomes, k):
    ind = findNearestNeighbours(point, neighbouringPoints, k)
    return majority_vote(outcomes[ind])

def genSyntData(n=50):
    random1 = ss.norm(0, 1).rvs((n, 2))
    random2 = ss.norm(1, 1).rvs((n, 2))
    points = np.concatenate((random1, random2), axis=0)
    outcomes = np.concatenate((np.repeat(0, n), np.repeat(1, n)))
    return (points, outcomes)

n=50
predictors, outcomes = genSyntData(n)

def makePredictionGrid(predictors, outcomes, limits, h, k):
    (x_min, x_max, y_min, y_max) = limits
    xs = np.arange(x_min, x_max, h)
    ys = np.arange(y_min, y_max, h)
    xx, yy = np.meshgrid(xs, ys)

    predictionGrid = np.zeros(xx.shape, dtype = int)
    for i,x in enumerate(xs):
        for j,y in enumerate(ys):
            p = np.array([x,y])
            predictionGrid[j,i] = kNN(p, predictors, outcomes, k)
    
    return (xx, yy, predictionGrid)


def plot_prediction_grid(xx, yy, prediction_grid, filename):
    """ Plot KNN predictions for every point on the grid."""
    from matplotlib.colors import ListedColormap
    background_colormap = ListedColormap(
        ["hotpink", "lightskyblue", "yellowgreen"])
    observation_colormap = ListedColormap(["red", "blue", "green"])
    plt.figure(figsize=(10, 10))
    plt.pcolormesh(xx, yy, prediction_grid,
                   cmap=background_colormap, alpha=0.5)
    plt.scatter(predictors[:, 0], predictors[:, 1],
                c=outcomes, cmap=observation_colormap, s=50)
    plt.xlabel('Variable 1')
    plt.ylabel('Variable 2')
    plt.xticks(())
    plt.yticks(())
    plt.xlim(np.min(xx), np.max(xx))
    plt.ylim(np.min(yy), np.max(yy))
    plt.savefig(filename)

k=5; filename = "knn_synth_1.pdf"; limits=(-3,4,-3,4); h = 0.1
(xx, yy, predictionGrid) = makePredictionGrid(predictors, outcomes, limits, h, k)
# plot_prediction_grid(xx, yy, predictionGrid, filename)


# plt.figure()
# plt.plot(points[:n, 0], points[:n, 1], 'ro')
# plt.plot(points[n:, 0], points[n:, 1], 'bo')
# plt.show()


# plt.plot(points[:,0], points[:,1], "ro")
# plt.plot(p[0], p[1], "bo")
# plt.show()

##Applying kNN Method


iris = datasets.load_iris()

print(iris)
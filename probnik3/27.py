from math import *

f = open('27B.txt')
data = []
for line in f:
    line = line.replace(',', '.')
    data.append([float(x) for x in line.split()])

print(len(data))

def get_clust(p0):
    cluster = [p for p in data if dist(p0, p) < 1]
    if len(cluster) != 0:
        for p in cluster: data.remove(p)
        next_clus = [get_clust(p) for p in cluster]
        cluster += sum(next_clus, [])
    return cluster

clusters = []
while len(data) != 0:
    cluster = get_clust(data[0])
    print(len(cluster))
    clusters.append(cluster)

def centroid(cluster):
    m = []
    for p in cluster:
        sm = sum(dist(p, p1) for p1 in cluster)
        m.append([sm, p])
    return min(m)[1]

centroids = [centroid(cluster) for cluster in clusters]
px = int(sum(x for x, y in centroids) / len(centroids) * 100000)
py = int(sum(y for x, y in centroids) / len(centroids) * 100000)
print(px,py)


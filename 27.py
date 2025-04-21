# from math import dist
#
# f = open('27_A_20911.txt')
# data = []
# for line in f:
#     line = line.replace(',', '.')
#     data.append([float(x) for x in line.split()])
#
# # собираем кластер
# def get_clust(p0):
#     cluster = [p for p in data if dist(p0, p) < 2]
#     if len(cluster) != 0:
#         for p in cluster: data.remove(p)
#         next_clusters = [get_clust(p) for p in cluster]
#         cluster += sum(next_clusters, [])
#     return cluster
#
#
# clusters = []
# while len(data) != 0:
#     cluster = get_clust(data[0])
#     print(len(cluster))
#     clusters.append(cluster)
#
#
# def centroid(cluster):
#     m = []
#     for p in cluster:
#         sm = sum(dist(p, p1) for p1 in cluster)
#         m.append([sm, p])
#     return min(m)[1]
#
# centroids = [centroid(cluster) for cluster in clusters]
# Px = int(sum(x for x, y in centroids)/len(centroids) * 10000)
# Py = int(sum(y for x, y in centroids)/len(centroids) * 10000)
# print(abs(Px), abs(Py))

from math import dist

f = open('27A_20295.txt')

data = []
for line in f:
    data.append([float(x) for x in line.split()])

def get_clust(p0):
    cluster = [p for p in data if dist(p0,p) < 1]
    if len(cluster) != 0:
        for p in cluster: data.remove(p)
        next_cluster = [get_clust(p) for p in cluster]
        cluster += sum(next_cluster, [])
    return cluster

clusters = []
while len(data) != 0:
    cluster = get_clust(data[0])
    clusters.append(cluster)

def plot(cluster):
    m =[]
    for p in cluster:
        sm = len(dist(p,p1) for p1 in cluster)
        m.append(sum)
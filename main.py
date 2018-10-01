import math
import time

from aco import ACO, Graph
from plot import plot


def distance(city1: dict, city2: dict):
    return math.sqrt((city1['x'] - city2['x']) ** 2 + (city1['y'] - city2['y']) ** 2)


# def main():
#     cities = []
#     points = []
#     with open('./data/chn31.txt') as f:
#         for line in f.readlines():
#             city = line.split(' ')
#             cities.append(dict(index=int(city[0]), x=int(city[1]), y=int(city[2])))
#             points.append((int(city[1]), int(city[2])))
#     cost_matrix = []
#     rank = len(cities)
#     for i in range(rank):
#         row = []
#         for j in range(rank):
#             row.append(distance(cities[i], cities[j]))
#         cost_matrix.append(row)
#     aco = ACO(10, 100, 1.0, 10.0, 0.5, 10, 2)
#     graph = Graph(cost_matrix, rank)
#     path, cost = aco.solve(graph)
#     print('cost: {}, path: {}'.format(cost, path))
#     plot(points, path)

# if __name__ == '__main__':
#     main()

def main():
    cities = []
    points = []
    with open('data/qatar.txt') as f:
        for line in f.readlines():
            city = line.split()
            cities.append(dict(index=int(city[0]), x=float(city[1]), y=float(city[2])))
            points.append((float(city[1]), float(city[2])))
    cost_matrix = []
    rank = len(cities)
    for i in range(rank):
        row = []
        for j in range(rank):
            row.append(distance(cities[i], cities[j]))
        cost_matrix.append(row)
    aco = ACO(ant_count=10, time_limit=60, generations=0, alpha=1.0, beta=10.0, rho=0.5, q=10, strategy=2)
    graph = Graph(cost_matrix, rank)
    path, cost, time = aco.solve(graph)
    print("Elapsed time was {0:.1f} seconds.".format(time))
    print('cost: {}, path: {}'.format(cost, path))
    # plot(points, path)

if __name__ == '__main__':
    main()

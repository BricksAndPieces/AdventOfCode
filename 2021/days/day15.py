"""
--- Day 15: Chiton ---
https://adventofcode.com/2021/day/15
"""

from collections import defaultdict
from itertools import product
import heapq

from aoc import *


# Dijkstra credit: https://git.io/JDujV
# Faster to use existing implementation than reimplement
class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = defaultdict(list)
        self.distances = {}

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[from_node, to_node] = distance


def dijkstra(graph, initial):
    visited = {initial: 0}
    h = [(0, initial)]
    path = {}
    nodes = set(graph.nodes)

    while nodes and h:
        current_weight, min_node = heapq.heappop(h)
        try:
            while min_node not in nodes:
                current_weight, min_node = heapq.heappop(h)
        except IndexError:
            break

        nodes.remove(min_node)

        for v in graph.edges[min_node]:
            weight = current_weight + graph.distances[min_node, v]
            if v not in visited or weight < visited[v]:
                visited[v] = weight
                heapq.heappush(h, (weight, v))
                path[v] = min_node

    return visited, path


def solve(tile):
    g = Graph({*product(range(len(tile[0])), range(len(tile)))})
    for (x, y) in g.nodes:
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= x + dx < len(tile) and 0 <= y + dy < len(tile[0]):
                g.add_edge((x, y), (x + dx, y + dy), tile[x + dx][y + dy])

    visited, _ = dijkstra(g, (0, 0))
    return visited[(len(tile[0]) - 1, len(tile) - 1)]


inputs = puzzle_input(15, 2021, sample=False).split('\n')
inputs_1 = [[int(x) for x in a] for a in inputs]

print(f'Part 1: {solve(inputs_1)}')

inputs_2 = [
    reduce(
        lambda a, b: [x if x else 9 for x in a + b],
        [[(cur + row + col) % 9 for cur in line] for col in range(5)]
    ) for row in range(5) for line in inputs_1
]

print(f'Part 2: {solve(inputs_2)}')

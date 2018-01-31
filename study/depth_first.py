graph1 = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}


def depth_first_search(graph, node, cache=[]):
    if node not in cache:
        cache.append(node)
        for n in graph[node]:
            depth_first_search(graph, n, cache)

    return cache

visited = depth_first_search(graph1,'A', [])
print(visited)

import collections


def breadth_first_search(graph, root):
    visited, queue = set(), collections.deque([root])
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                print(neighbour)
                visited.add(neighbour)
                queue.append(neighbour)


graph = {0: [1, 2], 1: [2], 2: []}
print(breadth_first_search(graph, 0))

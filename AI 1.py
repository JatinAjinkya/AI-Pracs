
from queue import Queue

romaniaMap = {'Oradea': ['Zerind', 'Sibiu'],
              'Zerind': ['Oradea', 'Arad'],
              'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
              'Timisoara': ['Arad', 'Lugoj'],
              'Lugoj': ['Timisoara', 'Mehadia'],
              'Mehadia': ['Lugoj', 'Drobeta'],
              'Drobeta': ['Mehadia', 'Craiova'],
              'Craiova': ['Drobeta', 'Rimnicu', 'Pitesti'],
              'Pitesti': ['Rimnicu', 'Craiova', 'Bucharest'],
              'Sibiu': ['Oradea', 'Fagaras', 'Rimnicu', 'Arad'],
              'Fagaras': ['Sibiu', 'Bucharest'],
              'Rimnicu': ['Sibiu', 'Pitesti', 'Craiova'],
              'Bucharest': ['Urziceni', 'Giurgiu'],
              'Giurgiu': ['Bucharest'],
              'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
              'Vaslui': ['Lasi', 'Urziceni'],
              'Lasi': ['Neamt', 'Vaslui'],
              'Neamt': ['Lasi'],
              'Hirsova': ['Urziceni', 'Eforie'],
              'Eforie': ['Hirsova']
              }


def bfs(startingNode, destinationNode):
    # For keeping track of what we have visited
    visited = {}
    # keep track of distance
    distance = {}
    # parent node of specific graph
    parent = {}

    bfs_traversal_output = []
    # BFS is queue based so using 'Queue' from python built-in
    queue = Queue()

    # travelling the cities in map
    for city in romaniaMap.keys():
        # since intially no city is visited so there will be nothing in visited list
        visited[city] = False
        parent[city] = None
        distance[city] = -1

    # starting from 'Specific city'
    startingCity = startingNode
    visited[startingCity] = True
    distance[startingCity] = 0
    queue.put(startingCity)

    while not queue.empty():
        u = queue.get()  # first element of the queue, here it will be 'first city'
        bfs_traversal_output.append(u)

        # explore the adjacent cities
        for v in romaniaMap[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                distance[v] = distance[u] + 1
                queue.put(v)

        # reaching our destination city
    g = destinationNode
    path = []
    while g is not None:
        path.append(g)
        g = parent[g]

    path.reverse()
    # printing the path to our destination city
    print(path)


# Starting City & Destination City
bfs('Oradea', 'Craiova')

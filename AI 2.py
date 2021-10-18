graph = {'Oradea': ['Zerind', 'Sibiu'],
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
visited = set()
def dfs(visited, graph, node):
 if node not in visited:
  print(node)
  visited.add(node)
  for neighbours in graph[node]:
   dfs(visited, graph, neighbours)
dfs(visited, graph, "Lugoj")

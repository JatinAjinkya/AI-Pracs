graph={
    "Oradea":["Zerind","Sibiu"],
    "Zerind":["Oradea","Arad"],
    "Arad":["Zerind","Sibiu","Timisoara"],
    "Timisoara":["Arad","Lugoj"],
    "Lugoj":["Timisoara","Mehadia"],
    "Mehadia":["Lugoj","Drobeta"],
    "Drobeta":["Mehadia","Craiova"],
    "Craiova":["Drobeta","Rimnicu","Pitesti"],
    "Pitesti":["Rimnicu","Craiova","Bucharest"],
    "Rimnicu":["Sibiu","Pitesti","Craiova"],
    "Sibiu":["Oradea","Fagaras","Rimnicu","Arad"],
    "Fagaras":["Sibiu","Bucharest"],
    "Bucharest":["Pitesti","Urziceni","Giurgiu","Fagaras"],
    "Giurgiu":["Bucharest"],
    "Urziceni":["Bucharest","Vaslui","Hirsova"],
    "Hirsova":["Urziceni","Eforie"],
    "Eforie":["Hirsova"],
    "Vaslui":["Lasi","Urziceni"],
    "Lasi":["Neamt","Vaslui"],
    "Neamt":["Lasi"]
    }

def dls(graph,node,visited,end,level,md):
    print("Current level:",level)
    print("Testing for",node)
    e = "Error the max depth is not enough"
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            if level >= md:
                return e
            if visited[-1] == end: #visited[-1] = last node of visited set
                return visited
            dls(graph,n,visited,end,level + 1, md)
    return e
path = []
node = input("Enter source node:")
end = input("Enter goal node:")
md = int(input("Enter max depth:"))
print(dls(graph,node,path,end,0,md))

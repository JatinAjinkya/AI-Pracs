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


def iddfs(g, n, seen, dst, dep, lim):
    if n not in seen:
        seen.append(n)
        if dep <= lim:
            for i in g[n]:
                if seen[-1] is dst:
                    return seen
                iddfs(g, i, seen, dst, dep + 1, lim)
        else:
            print("Maximum limit reached")
    return None


print(iddfs(graph, 'Arad', [], 'Hirsova', 0, int(input("Enter max limit: "))))

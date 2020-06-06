graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited=[]
queue=[]

def dfs(visited,graph,node):
    queue.append(node)
    print(queue)
    while queue:
        while queue:
            s = queue.pop(0)
            visited.append(node)
            for i in graph[s]:
                if i not in visited:
                    queue.insert(1,i)
                    print(queue)




dfs(visited,graph,'A')
def hopcroft_karp(graph, left_nodes, right_nodes):
    def bfs():
        for node in left_nodes:
            if matching[node] is None:
                distance[node] = 0
                queue.append(node)
            else:
                distance[node] = float('inf')
        
        distance[None] = float('inf')
        
        while queue:
            curr_node = queue.popleft()
            if distance[curr_node] < distance[None]:
                for neighbor in graph[curr_node]:
                    if distance[matching[neighbor]] == float('inf'):
                        distance[matching[neighbor]] = distance[curr_node] + 1
                        queue.append(matching[neighbor])
        
        return distance[None] != float('inf')
    
    def dfs(curr_node):
        if curr_node is not None:
            for neighbor in graph[curr_node]:
                if distance[matching[neighbor]] == distance[curr_node] + 1 and dfs(matching[neighbor]):
                    matching[neighbor] = curr_node
                    matching[curr_node] = neighbor
                    return True
            distance[curr_node] = float('inf')
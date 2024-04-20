def ford_fulkerson(graph, source, sink):
    def dfs(curr_node, curr_flow):
        visited.add(curr_node)
        if curr_node == sink:
            return curr_flow
        for neighbor, capacity in graph[curr_node].items():
            if neighbor not in visited and capacity > 0:
                path_flow = dfs(neighbor, min(curr_flow, capacity))
                if path_flow > 0:
                    graph[curr_node][neighbor] -= path_flow
                    graph[neighbor][curr_node] += path_flow
                    return path_flow
        return 0
    
    max_flow = 0
    while True:
        visited = set()
        path_flow = dfs(source, float('inf'))
        if path_flow == 0:
            break
        max_flow += path_flow
    
    return max_flow
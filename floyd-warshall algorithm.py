def floyd_warshall(graph):
    dist = {node: {v: float('inf') for v in graph} for node in graph}
    for node in graph:
        dist[node][node] = 0
        for neighbor, weight in graph[node].items():
            dist[node][neighbor] = weight
    
    for k in graph:
        for i in graph:
            for j in graph:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist
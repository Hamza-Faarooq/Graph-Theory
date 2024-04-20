from collections import deque

def edmonds_karp(graph, source, sink):
    max_flow = 0
    while True:
        parent = {node: None for node in graph}
        parent[source] = source
        queue = deque([source])
        
        while queue:
            curr_node = queue.popleft()
            for neighbor, capacity in graph[curr_node].items():
                if parent[neighbor] is None and capacity > 0:
                    parent[neighbor] = curr_node
                    queue.append(neighbor)
                    if neighbor == sink:
                        break
        
        if parent[sink] is None:
            break
        
        path_flow = float('inf')
        node = sink
        while node != source:
            path_flow = min(path_flow, graph[parent[node]][node])
            node = parent[node]
        
        max_flow += path_flow
        node = sink
        while node != source:
            graph[parent[node]][node] -= path_flow
            graph[node][parent[node]] += path_flow
            node = parent[node]
    
    return max_flow
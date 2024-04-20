import heapq

def prim(graph):
    visited = set()
    min_span_tree = []
    start = next(iter(graph))
    pq = [(0, start)]
    
    while pq:
        cost, node = heapq.heappop(pq)
        if node not in visited:
            visited.add(node)
            min_span_tree.append((node, cost))
            for neighbor, weight in graph[node].items():
                if neighbor not in visited:
                    heapq.heappush(pq, (weight, neighbor))
    
    return min_span_tree
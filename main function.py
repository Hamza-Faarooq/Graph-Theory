import heapq
from collections import deque

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        if curr_dist > distances[curr_node]:
            continue
        
        for neighbor, weight in graph[curr_node].items():
            dist = curr_dist + weight
            if dist < distances[neighbor]:
                distances[neighbor] = dist
                heapq.heappush(pq, (dist, neighbor))
    
    return distances
    
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
 
class DisjointSet:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        self.rank = {node: 0 for node in nodes}
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)
        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal(graph):
    edges = [(graph[u][v], u, v) for u in graph for v in graph[u]]
    edges.sort()
    nodes = set(node for node in graph)
    min_span_tree = []
    ds = DisjointSet(nodes)
    
    for cost, u, v in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            min_span_tree.append((u, v, cost))
    
    return min_span_tree

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
            return False
    
    matching = {node: None for node in left_nodes}
    distance = {}
    queue = deque()
    max_matching = 0
    
    while bfs():
        for node in left_nodes:
            if matching[node] is None and dfs(node):
                max_matching += 1
    
    return max_matching

def main():
    # Example graph representations
    weighted_graph = {
        'A': {'B': 4, 'C': 3},
        'B': {'A': 4, 'C': 2, 'D': 3},
        'C': {'A': 3, 'B': 2, 'D': 1},
        'D': {'B': 3, 'C': 1}
    }
    
    unweighted_graph = {
        'A': {'B', 'C'},
        'B': {'A', 'C', 'D'},
        'C': {'A', 'B', 'D'},
        'D': {'B', 'C'}
    }
    
    flow_network = {
        'S': {'A': 10, 'B': 10},
        'A': {'C': 5, 'D': 15},
        'B': {'C': 15, 'D': 10},
        'C': {'T': 10},
        'D': {'T': 10}
    }
    
    # Dijkstra's Algorithm
    shortest_paths = dijkstra(weighted_graph, 'A')
    print("Shortest Paths from 'A':", shortest_paths)
    
    # Floyd-Warshall Algorithm
    all_pairs_shortest_paths = floyd_warshall(weighted_graph)
    print("All Pairs Shortest Paths:", all_pairs_shortest_paths)
    
    # Prim's Algorithm
    min_span_tree_prim = prim(weighted_graph)
    print("Minimum Spanning Tree (Prim's Algorithm):", min_span_tree_prim)
    
    # Kruskal's Algorithm
    min_span_tree_kruskal = kruskal(weighted_graph)
    print("Minimum Spanning Tree (Kruskal's Algorithm):", min_span_tree_kruskal)
    
    # Ford-Fulkerson Algorithm
    max_flow_ford_fulkerson = ford_fulkerson(flow_network, 'S', 'T')
    print("Maximum Flow (Ford-Fulkerson Algorithm):", max_flow_ford_fulkerson)
    
    # Edmonds-Karp Algorithm
    max_flow_edmonds_karp = edmonds_karp(flow_network, 'S', 'T')
    print("Maximum Flow (Edmonds-Karp Algorithm):", max_flow_edmonds_karp)
    
    # Hopcroft-Karp Algorithm (Example bipartite graph)
    bipartite_graph = {
        'L1': {'R1', 'R2'},
        'L2': {'R2'},
        'L3': {'R2', 'R3'},
        'L4': {'R3'}
    }
    left_nodes = {'L1', 'L2', 'L3', 'L4'}
    right_nodes = {'R1', 'R2', 'R3'}
    max_matching_hopcroft_karp = hopcroft_karp(bipartite_graph, left_nodes, right_nodes)
    print("Maximum Cardinality Matching (Hopcroft-Karp Algorithm):", max_matching_hopcroft_karp)

if __name__ == "__main__":
    main()
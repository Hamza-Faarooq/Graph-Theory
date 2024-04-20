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
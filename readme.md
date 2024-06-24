# This is a part of Graph Theory course used in ML & Robotics. 


# Dijkstra's Algorithm



## What it is
Dijkstra's algorithm is a graph search algorithm that solves the single-source shortest path problem for a graph with non-negative edge weights, producing a shortest path tree.

## Why it is used
This algorithm is used to find the shortest paths from a source vertex to all other vertices in a graph, which is essential in optimizing routes and minimizing travel costs.

## Where it is used
- **Network Routing Protocols**: To find the shortest path for data packet transmission.
- **Geographic Information Systems (GIS)**: For route planning and navigation.
- **Robotics and AI**: In pathfinding and motion planning.
- **Transportation Networks**: To optimize travel routes and schedules.

## How it works
1. Initialize distances from the source to all vertices as infinite and distance to the source itself as zero.
2. Use a priority queue to repeatedly extract the vertex with the minimum distance.
3. For the extracted vertex, update the distance for all its adjacent vertices.
4. Repeat until all vertices are processed.


# Hopcroft-Karp Algorithm

## What it is
The Hopcroft-Karp algorithm is an algorithm that finds a maximum matching in a bipartite graph in O(E√V) time, where E is the number of edges and V is the number of vertices.

## Why it is used
It efficiently finds the largest possible matching in a bipartite graph, which is crucial for optimization problems where elements from two sets need to be paired.

## Where it is used
- **Job Assignment Problems**: Assigning tasks to workers in the most efficient manner.
- **Network Flows**: Finding maximum matchings in network flow problems.
- **Scheduling**: Pairing tasks with time slots or resources.

## How it works
1. Repeatedly search for augmenting paths using BFS.
2. Use DFS to augment the matching along these paths.
3. Repeat until no more augmenting paths can be found.



# Edmunds-Karp Algorithm

## What it is
The Edmonds-Karp algorithm is an implementation of the Ford-Fulkerson method for computing the maximum flow in a flow network. It uses BFS to find augmenting paths.

## Why it is used
It provides a simple and intuitive way to find the maximum flow in a network, which is important for optimizing network throughput.

## Where it is used
- **Network Routing**: To maximize data flow in communication networks.
- **Telecommunications**: For bandwidth allocation and network design.
- **Transportation Systems**: To optimize traffic flow.
- **Supply Chain Management**: For maximizing the flow of goods through a network.

## How it works
1. Initialize flow to zero.
2. Use BFS to find an augmenting path.
3. Increase the flow along the path.
4. Repeat until no more augmenting paths are found.



# Floyd-Warshall Algorithm

## What it is
The Floyd-Warshall algorithm is a dynamic programming algorithm for finding shortest paths between all pairs of vertices in a weighted graph with positive or negative edge weights.

## Why it is used
It finds shortest paths between all pairs of vertices, which is useful for solving many types of optimization problems involving pathfinding.

## Where it is used
- **Network Routing**: To find shortest paths in network topologies.
- **Urban Traffic Planning**: For determining shortest travel routes.
- **Operations Research**: In optimizing logistics and supply chains.
- **Game Development**: For AI pathfinding.

## How it works
1. Initialize a distance matrix with edge weights.
2. Update the matrix by considering all pairs of vertices.
3. Use an intermediate vertex to find shorter paths.
4. Repeat for all vertices.



# Ford-Fulkerson Algorithm

## What it is
The Ford-Fulkerson algorithm computes the maximum flow in a flow network by searching for augmenting paths and increasing the flow until no more paths are found.

## Why it is used
It is a fundamental algorithm for solving maximum flow problems in networks, which is essential for various optimization problems.

## Where it is used
- **Pipeline Network Design**: To maximize the flow of liquids or gases.
- **Image Segmentation**: In computer vision.
- **Bipartite Matching**: For matching problems in bipartite graphs.
- **Telecommunications**: To optimize the flow of data through networks.

## How it works
1. Start with zero flow.
2. While there is an augmenting path, increase the flow.
3. Use DFS or BFS to find paths.
4. Adjust the flows until no more augmenting paths exist.


# Kruskal's Algorithm

## What it is
Kruskal's algorithm is a minimum spanning tree algorithm that adds edges to the spanning tree in increasing order of their weights.

## Why it is used
It efficiently finds a minimum spanning tree, which is important for optimizing the total weight of edges in a network.

## Where it is used
- **Network Design**: To design least-cost networks.
- **Clustering**: In machine learning for hierarchical clustering.
- **Electric Grid Design**: To minimize the cost of laying cables.
- **Transportation Networks**: For designing efficient road or rail networks.

## How it works
1. Sort all edges in non-decreasing order of their weight.
2. Pick the smallest edge.
3. Check if it forms a cycle with the spanning tree formed so far.
4. If no cycle is formed, include this edge. Otherwise, discard it.
5. Repeat until there are (V-1) edges in the spanning tree.



# Prim's Algorithm

## What it is
Prim's algorithm is a minimum spanning tree algorithm that grows the spanning tree by adding the cheapest possible connection from the tree to another node.

## Why it is used
It finds a minimum spanning tree for a weighted undirected graph, which minimizes the total weight of the edges.

## Where it is used
- **Telecommunications**: For designing efficient communication networks.
- **Water Supply Networks**: To minimize the cost of pipelines.
- **Computer Networks**: For network design and optimization.
- **Civil Engineering**: In the planning and construction of infrastructure.

## How it works
1. Initialize a tree with a single vertex.
2. Grow the tree by adding the smallest edge from the tree to a new vertex.
3. Repeat until all vertices are included in the tree.


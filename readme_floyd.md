### Floyd-Warshall Algorithm

```markdown
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


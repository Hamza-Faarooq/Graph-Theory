### Kruskal's Algorithm

```markdown
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


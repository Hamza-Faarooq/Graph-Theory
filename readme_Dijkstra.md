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


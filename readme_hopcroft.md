### Hopcroft-Karp Algorithm

```markdown
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


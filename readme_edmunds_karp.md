### Edmunds-Karp Algorithm

```markdown
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


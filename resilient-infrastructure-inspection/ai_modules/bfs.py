"""CO2: Breadth-first search. Finds a path with the fewest edges (not lowest weighted cost)."""
from collections import deque

def bfs(graph, start, goal):
    queue = deque([start])
    parent = {start: None}
    expanded = 0
    while queue:
        node = queue.popleft()
        expanded += 1
        if node == goal:
            break
        for neighbor, _cost in graph.get(node, []):
            if neighbor not in parent:
                parent[neighbor] = node
                queue.append(neighbor)
    if goal not in parent:
        return {"path": [], "cost": None, "expanded": expanded}
    path, cur = [], goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    # Report weighted cost of the path BFS found.
    cost = 0
    for a, b in zip(path, path[1:]):
        cost += next(c for n, c in graph[a] if n == b)
    return {"path": path, "cost": cost, "expanded": expanded}

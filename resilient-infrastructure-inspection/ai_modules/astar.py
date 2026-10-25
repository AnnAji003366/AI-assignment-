"""CO2: A* search with a zero heuristic by default (equivalent to uniform-cost search)."""
import heapq

def astar(graph, start, goal, heuristic=None):
    if heuristic is None:
        heuristic = lambda _node: 0
    frontier = [(heuristic(start), 0, start)]
    parent = {start: None}
    best_cost = {start: 0}
    expanded = 0
    while frontier:
        _f, cost_so_far, node = heapq.heappop(frontier)
        if cost_so_far != best_cost.get(node):
            continue
        expanded += 1
        if node == goal:
            break
        for neighbor, edge_cost in graph.get(node, []):
            new_cost = cost_so_far + edge_cost
            if new_cost < best_cost.get(neighbor, float("inf")):
                best_cost[neighbor] = new_cost
                parent[neighbor] = node
                heapq.heappush(frontier, (new_cost + heuristic(neighbor), new_cost, neighbor))
    if goal not in best_cost:
        return {"path": [], "cost": None, "expanded": expanded}
    path, cur = [], goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return {"path": path, "cost": best_cost[goal], "expanded": expanded}

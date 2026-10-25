# CO2 — Search comparison

Run the dashboard with the same start and destination for both algorithms.

- BFS explores by number of edges and is optimal in an unweighted graph. With weighted roads, it may not minimize total travel cost.
- A* evaluates `f(n) = g(n) + h(n)`. The current implementation uses `h(n) = 0` because the dataset has no validated geometric heuristic. This is admissible and makes A* equivalent to uniform-cost search.
- Record the path, weighted cost, and expanded-node count shown by the application for your chosen test case.

Do not invent or pre-fill results: paste the actual output observed on your machine. A practical future improvement is to add coordinates and a justified admissible distance heuristic.

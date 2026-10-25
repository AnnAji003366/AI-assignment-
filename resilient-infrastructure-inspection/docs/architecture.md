# System architecture

1. Load synthetic sites, roads, and crew data from JSON.
2. CO1 agent ranks sites by severity.
3. CO2 searches the road graph using BFS and A*.
4. CO3 CSP assigns tasks to eligible crews using backtracking and forward checking.
5. CO4 knowledge base derives high-priority and urgent structural flags.
6. Streamlit displays results and scenario controls.

```text
Synthetic JSON data
        |
        v
  CO1 Priority Agent
        |
        +------> CO2 BFS / A* route search
        |
        +------> CO3 CSP crew allocation
        |
        +------> CO4 Facts / Rules / Inference
        |
        v
 Streamlit results dashboard
```

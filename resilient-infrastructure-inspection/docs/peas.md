# CO1 — PEAS description

| Element | Description |
|---|---|
| Performance measure | Prioritize severe damage, generate valid crew allocations, find routes, reduce travel cost. |
| Environment | Simulated infrastructure sites, road graph, crews, skill and time constraints. |
| Actuators | Recommend priority order, routes, crew assignments and alerts. |
| Sensors | Site reports, severity, duration, road status, crew skills and available hours. |

## Assumptions
- All data are synthetic and for classroom demonstration only.
- Road costs are simulated travel-cost units, not real distances or travel times.
- Severity labels are supplied as input; the prototype does not detect damage from images.
- Crew allocation is a simplified planning problem and does not certify infrastructure safety.

## Performance measures
- Whether a route is found when a path exists.
- Search path cost and number of expanded nodes.
- Whether every task receives a qualified crew without exceeding hours or task limits.
- Whether inference conclusions follow from the encoded facts and rules.

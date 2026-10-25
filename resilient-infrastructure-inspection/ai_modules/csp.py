"""CO3: Crew allocation CSP using backtracking and forward checking."""
def solve_csp(tasks, crews):
    # Each task variable's domain contains crews with the required skill and enough hours.
    domains = {}
    for task in tasks:
        domains[task["id"]] = [
            crew["id"] for crew in crews
            if task["required_skill"] in crew["skills"]
            and crew["available_hours"] >= task["duration"]
        ]

    assignment = {}
    remaining_hours = {c["id"]: c["available_hours"] for c in crews}
    remaining_tasks = {c["id"]: c["max_tasks"] for c in crews}
    crew_by_id = {c["id"]: c for c in crews}
    nodes = 0

    # Most-constrained variable first: tasks with the smallest domain.
    ordered_tasks = sorted(tasks, key=lambda t: (len(domains[t["id"]]), -t["priority"]))

    def backtrack(index):
        nonlocal nodes
        nodes += 1
        if index == len(ordered_tasks):
            return True
        task = ordered_tasks[index]
        for crew_id in domains[task["id"]]:
            if remaining_hours[crew_id] < task["duration"] or remaining_tasks[crew_id] <= 0:
                continue
            assignment[task["id"]] = crew_id
            remaining_hours[crew_id] -= task["duration"]
            remaining_tasks[crew_id] -= 1

            # Forward checking: each unassigned task must still have at least one feasible crew.
            feasible = True
            for other in ordered_tasks[index+1:]:
                if not any(
                    remaining_hours[cid] >= other["duration"] and remaining_tasks[cid] > 0
                    for cid in domains[other["id"]]
                ):
                    feasible = False
                    break
            if feasible and backtrack(index + 1):
                return True

            remaining_hours[crew_id] += task["duration"]
            remaining_tasks[crew_id] += 1
            assignment.pop(task["id"], None)
        return False

    success = backtrack(0)
    return {
        "success": success,
        "assignment": assignment.copy() if success else {},
        "domains": domains,
        "nodes": nodes
    }

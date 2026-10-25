"""CO4: Small fact/rule knowledge base with forward chaining and trace."""
def infer(sites, crews):
    facts, trace = set(), []
    for site in sites:
        facts.add(("severity", site["id"], site["severity"]))
        facts.add(("skill", site["id"], site["required_skill"]))
        trace.append(f"FACT: {site['id']} severity is {site['severity']}.")
        if site["severity"] == "High":
            facts.add(("high_priority", site["id"]))
            trace.append(f"RULE: severity({site['id']}, High) -> high_priority({site['id']}).")
        if site["severity"] == "High" and site["required_skill"] == "Structural":
            facts.add(("urgent_structural", site["id"]))
            trace.append(f"RULE: high severity and Structural skill -> urgent_structural({site['id']}).")

    qualified = set()
    for site in sites:
        for crew in crews:
            if site["required_skill"] in crew["skills"]:
                qualified.add((site["id"], crew["id"]))
                facts.add(("qualified", site["id"], crew["id"]))
    trace.append("QUERY 1: Which sites are high priority?")
    q1 = sorted(f[1] for f in facts if len(f) == 2 and f[0] == "high_priority")
    trace.append(f"CONCLUSION: {q1 if q1 else 'None'}")
    trace.append("QUERY 2: Which sites require urgent structural inspection?")
    q2 = sorted(f[1] for f in facts if len(f) == 2 and f[0] == "urgent_structural")
    trace.append(f"CONCLUSION: {q2 if q2 else 'None'}")
    return {"facts": sorted([str(x) for x in facts]), "high_priority_sites": q1,
            "urgent_structural_sites": q2, "qualified_pairs": sorted([list(x) for x in qualified]),
            "trace": trace}

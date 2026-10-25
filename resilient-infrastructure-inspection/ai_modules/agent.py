"""CO1: Simple intelligent-agent description and priority ordering."""
def peas():
    return {
        "Performance": "Prioritize severe risks, produce valid assignments, reduce travel cost.",
        "Environment": "Simulated inspection sites, road network, and inspection crews.",
        "Actuators": "Recommend priority order, routes, and crew assignments.",
        "Sensors": "Site severity, inspection duration, road costs, crew skills and availability."
    }

def prioritize_sites(sites):
    rank = {"High": 3, "Medium": 2, "Low": 1}
    return sorted(sites, key=lambda s: (rank.get(s["severity"], 0), s.get("priority", 0)), reverse=True)

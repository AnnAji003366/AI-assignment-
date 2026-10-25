import json
from pathlib import Path
import streamlit as st
from ai_modules.agent import peas, prioritize_sites
from ai_modules.bfs import bfs
from ai_modules.astar import astar
from ai_modules.csp import solve_csp
from ai_modules.knowledge_base import infer

BASE = Path(__file__).parent

def load_json(filename):
    with open(BASE / "data" / filename, "r", encoding="utf-8") as f:
        return json.load(f)

sites = load_json("sites.json")
roads = load_json("roads.json")
crews = load_json("crews.json")

def make_graph(roads, blocked=None):
    graph = {}
    blocked = blocked or set()
    for road in roads:
        a, b, cost = road["from"], road["to"], road["cost"]
        if frozenset((a, b)) in blocked:
            continue
        graph.setdefault(a, []).append((b, cost))
        graph.setdefault(b, []).append((a, cost))
    return graph

st.set_page_config(page_title="Resilient Infrastructure Inspection", page_icon="🏗️", layout="wide")
st.title("🏗️ AI-Based Resilient Infrastructure Inspection")
st.caption("CST401 Artificial Intelligence | Group 6 | SDG 9 and SDG 11")
st.info("Demonstration uses synthetic data. It is an educational prototype, not a real safety assessment tool.")

with st.sidebar:
    st.header("Scenario controls")
    blocked_road = st.selectbox("Road condition", ["All roads open", "Block road B–C", "Block road D–E"])
    if blocked_road == "Block road B–C":
        blocked = {frozenset(("B", "C"))}
    elif blocked_road == "Block road D–E":
        blocked = {frozenset(("D", "E"))}
    else:
        blocked = set()
    crew_shortage = st.checkbox("Simulate crew shortage (remove Crew Gamma)")
    selected_crews = [c for c in crews if not (crew_shortage and c["id"] == "C3")]

graph = make_graph(roads, blocked)
st.subheader("1. Inspection sites")
st.dataframe(sites, use_container_width=True, hide_index=True)

col1, col2 = st.columns(2)
with col1:
    st.subheader("2. CO1 — Intelligent agent (PEAS)")
    st.json(peas())
    ordered = prioritize_sites(sites)
    st.write("Recommended inspection priority:")
    st.dataframe([{"Site": s["name"], "Severity": s["severity"], "Priority": s["priority"]} for s in ordered],
                 use_container_width=True, hide_index=True)

with col2:
    st.subheader("3. CO2 — Route search: BFS vs A*")
    nodes = sorted(graph.keys())
    start = st.selectbox("Start location", nodes, index=nodes.index("A") if "A" in nodes else 0)
    goal = st.selectbox("Destination", nodes, index=nodes.index("E") if "E" in nodes else len(nodes)-1)
    b = bfs(graph, start, goal)
    a = astar(graph, start, goal)
    st.write("**BFS** — fewest edges, weighted cost of its selected path")
    st.json(b)
    st.write("**A*** — with h(n)=0, equivalent to uniform-cost search")
    st.json(a)
    st.caption("A* uses h(n)=0 for this weighted graph because no validated geographic heuristic is supplied. This is admissible but less informed.")

st.subheader("4. CO3 — CSP crew allocation")
csp = solve_csp(ordered, selected_crews)
if csp["success"]:
    crew_map = {c["id"]: c["name"] for c in selected_crews}
    task_map = {s["id"]: s for s in sites}
    allocation = [{"Task": task_map[tid]["name"], "Required skill": task_map[tid]["required_skill"],
                   "Assigned crew": crew_map[cid], "Duration (hours)": task_map[tid]["duration"]}
                  for tid, cid in csp["assignment"].items()]
    st.success(f"Valid assignment found. Backtracking nodes visited: {csp['nodes']}")
    st.dataframe(allocation, use_container_width=True, hide_index=True)
else:
    st.error("No valid crew allocation exists under the current constraints.")
    st.write("Possible reason: skills, hours, or task-count limits leave at least one task without a feasible crew.")
st.write("**Initial domains (eligible crews):**")
st.json(csp["domains"])

st.subheader("5. CO4 — Knowledge representation and inference")
kb = infer(sites, selected_crews)
left, right = st.columns(2)
left.metric("High-priority sites", len(kb["high_priority_sites"]))
left.write(kb["high_priority_sites"])
right.metric("Urgent structural sites", len(kb["urgent_structural_sites"]))
right.write(kb["urgent_structural_sites"])
with st.expander("View facts and reasoning trace"):
    st.write("Facts:")
    st.code("\n".join(kb["facts"]))
    st.write("Inference trace:")
    st.code("\n".join(kb["trace"]))

st.subheader("6. Test scenario summary")
st.markdown(
    "- **Test 1:** All roads open and all crews available. Expect route results and a feasible allocation.\n"
    "- **Test 2:** Block road B–C or D–E. Search should adapt to the changed graph; some routes may cost more.\n"
    "- **Test 3:** Remove Crew Gamma. Check whether the CSP still finds a valid assignment; if not, it reports the constraint failure."
)
